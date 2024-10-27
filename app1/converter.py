def convert(feet, inches):
    feet_to_meter = float(feet*0.3048)
    inches_to_meter = float (inches*0.0254)
    meter = feet_to_meter + inches_to_meter
    return meter
