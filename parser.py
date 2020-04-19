from argparse import ArgumentParser
from collections import deque
import yaml
import re
from pprint import pprint
import video_objects as vo


def create_parser():
    parser = ArgumentParser()
    parser.add_argument("file", help="File to process")

    return parser


def parse_properties(properties):
    parsed_list = []
    for stage in properties:
        parsed = {}
        found_attr = False
        for prop in stage:
            var = prop.split('=')
            if var[0] == prop:
                if found_attr is True:
                    raise AttributeError('Multiple non-expr statements found')
                found_attr = True
                parsed["attr"] = var[0]
            else:
                try:
                    var, val = var
                except ValueError:
                    raise ValueError('You missed a comma somewhere.')
                if "->" in val:
                    val = list(map(lambda x: float(x.strip()),
                                   val.split('->')))
                else:
                    try:
                        val = float(val)
                    except (ValueError, TypeError):
                        try:
                            val = eval(val)
                        except NameError:
                            pass

                parsed[var] = val

        parsed_list.append(parsed)

    return parsed_list


def parse_into_class(stage):
    imported_styles = stage.get("imported_styles")
    if imported_styles is not None:
        del stage["imported_styles"]
        user_styles = yaml.load(open("styles.yaml", "r"),
                                Loader=yaml.FullLoader)
        try:
            assert isinstance(imported_styles, list)
            for style in imported_styles:
                try:
                    defined_style = user_styles.get(style)
                    for prop in defined_style:
                        stage[prop] = defined_style[prop]
                except TypeError:
                    raise ValueError(
                        f'{style} does not exist in user-defined styles.')

        except AssertionError:
            raise TypeError('imported_styles is not a list.')

    duration = stage.get("duration")
    t = stage.get("t")
    attr = stage.get("attr")
    disappear = stage.get("disappear")
    if t is not None:
        del stage["t"]
        del stage["attr"]
        del stage["duration"]

    if disappear is not None:
        del stage["disappear"]

    if not isinstance(t, list):
        t = [t]

    if not isinstance(duration, list):
        duration = [duration] * len(t)

    staged_values = {}
    other_attributes = {}

    for value in stage:
        attr_value = stage[value]
        if isinstance(attr_value, list):
            staged_values[value] = attr_value
        else:
            other_attributes[value] = attr_value

    if re.match("[\"'].*[\"']", attr):
        return vo.AnimatedText(attr[1:-1],
                               duration=duration,
                               start_value=t,
                               staged_values=staged_values,
                               del_time=disappear,
                               **other_attributes)


def parse_text(file_name):
    text_file = open(file_name, "r").read()
    stage_list = re.split(r"\[\d*\]:", text_file)

    stage_properties = []

    for stage in stage_list:
        code_stack = deque()
        properties = []
        count = 0
        enclosing_bracket = None
        for char in stage:
            if char == ',' and count == 0:
                properties.append("".join(code_stack).strip())
                code_stack = deque()
            elif char == "(":
                count += 1
                enclosing_bracket = ")"
                code_stack.append("(")
            elif char == "[":
                count += 1
                enclosing_bracket = "]"
                code_stack.append("[")
            elif char == ")" and enclosing_bracket == ")":
                count -= 1
                code_stack.append(")")
            elif char == "]" and enclosing_bracket == "]":
                count -= 1
                code_stack.append("]")
            else:
                code_stack.append(char)

        stage_properties.append(properties)

    stage_properties = list(filter(lambda x: x != [], stage_properties))
    parsed_prop = parse_properties(stage_properties)

    classes = [parse_into_class(stage) for stage in parsed_prop]

    return classes


def main():
    args = create_parser().parse_args()
    for i in parse_text(args.file):
        pprint(i.__dict__)


if __name__ == "__main__":
    main()
