def savings(gross_pay, tax_rate, expenses):
    '''savings'''
    after_tax_pay = gross_pay*(1-tax_rate)//1
    take_home_pay = int(after_tax_pay - expenses)
    return int(take_home_pay)

def material_waste (total_material, material_units, num_jobs, job_consumption):
    '''Material waste'''
    total_material_consumption = num_jobs*job_consumption
    remaining_total_material = total_material - total_material_consumption
    return f"{remaining_total_material}{material_units}"

def interest(principal,rate,periods):
    '''Interest'''
    simple_interest = principal*(rate*periods)
    final_investment_value = principal + simple_interest//1
    return int(final_investment_value)






