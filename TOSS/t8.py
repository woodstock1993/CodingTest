"""
    총 근로시간: total_hour

    추가 근로시간: extra_hour -> total_hour - 40

    시간 외 근무시간 (연장근로시간 + 야간근로시간 + 휴일근로시간 + 휴일연장근로시간)
        총 연장근로시간: sub_extra_hour
        총 야간근로시간: sub_night_hour
        총 휴일근로시간: sub_holiday_hour
        총 휴일연장근로시간: sub_extra_holiday_hour

    시간 외 근무수당 (기본급여 + 연장수당 + 야간수당 + 휴일수당 + 휴일연장수당)
        기본급여: basic_pay * 40
        연장수당: exceed_pay * sub_extra_hour
        야간수당: night_pay * sub_night_hour
        휴일수당: holiday_pay * sub_holiday_hour
        휴일연장수당: extra_holiday_pay * extra_extra_holiday_hour
"""


def calc_overtime_hour(total_hour):
    extra_hour = total_hour - 40
    if extra_hour <= 0:
        return
    sub_extra_hour = 'DB에서 개개인의 연장근무 시간 조회'
    sub_night_hour = 'DB에서 개개인의 야간근무시간 조회'
    sub_holiday_hour = 'DB에서 개개인의 휴일근무시간 조회'
    extra_extra_holiday_hour = 'DB에서 개개인의 휴일연장근무시간 조회'

    return sub_extra_hour, sub_night_hour, sub_holiday_hour, extra_extra_holiday_hour


def calc_overtime_pay(basic_pay, sub_extra_hour, sub_night_hour, sub_holiday_hour, extra_extra_holiday_hour):

    pay = basic_pay * 1.5
    exceed_pay = pay * sub_extra_hour
    night_pay = pay * sub_night_hour
    holiday_pay = pay * sub_holiday_hour
    extra_holiday_pay = pay * extra_extra_holiday_hour

    overtime_payment = exceed_pay + night_pay + holiday_pay + extra_holiday_pay

    return overtime_payment


def calc(total_hour, basic_pay):

    basic_payment = basic_pay * 40

    overtime_pay = total_hour - 40

    if overtime_pay > 0:
        overtime_payment = calc_overtime_pay
        return basic_payment + overtime_payment

    return basic_payment

