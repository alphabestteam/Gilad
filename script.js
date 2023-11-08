/*
Your job for today is to finish the starSign function.

Find the astrological sign, given the birth details as a Date object.
Start and end dates for zodiac signs very on different resources, 
so we will use this table to get consistent testable results:

Aquarius ----- 21 January - 19 February
Pisces ----- 20 February - 20 March
Aries ----- 21 March - 20 April
Taurus ----- 21 April - 21 May
Gemini ----- 22 May - 21 June
Cancer ----- 22 June - 22 July
Leo ----- 23 July - 23 August
Virgo ----- 24 August - 23 September
Libra ----- 24 September - 23 October
Scorpio ------ 24 October - 22 November
Sagittarius ----- 23 November - 21 December
Capricon ------ 22 December - 20 January
*/

function starSign(date){
    const month = date.getMonth()
    const day = date.getDate()

    if ((month == 0 && day >= 21) || (month == 1 && day <= 19)){
        return "your astrological sign is Aquarius";
    }
    else if ((month == 1 && day >= 20) || (month == 2 && day <= 20)){
        return "your astrological sign is Pisces";
    }
    else if ((month == 2 && day >= 21) || (month == 3 && day <= 20)){
        return "your astrological sign is Aries";
    }
    else if ((month == 3 && day >= 21) || (month == 4 && day <= 21)){
        return "your astrological sign is Taurus";
    }
    else if ((month == 4 && day >= 22) || (month == 5 && day <= 21)){
        return "your astrological sign is Gemini";
    }
    else if ((month == 5 && day >= 22) || (month == 6 && day <= 22)){
        return "your astrological sign is Cancer";
    }
    else if ((month == 6 && day >= 23) || (month == 7 && day <= 23)){
        return "your astrological sign is Leo";
    }
    else if ((month == 7 && day >= 24) || (month == 8 && day <= 23)){
        return "your astrological sign is Virgo";
    }
    else if ((month == 8 && day >= 24) || (month == 9 && day <= 23)){
        return "your astrological sign is Libra";
    }
    else if ((month == 9 && day >= 24) || (month == 10 && day <= 22)){
        return "your astrological sign is Scorpio";
    }
    else if ((month == 10 && day >= 23) || (month == 11 && day <= 21)){
        return "your astrological sign is Sagittarius";
    }
    else if ((month == 11 && day >= 22) || (month == 0 && day <= 20)){
        return "your astrological sign is Capricon";
    }

}


const date = new Date("2004-01-22");
console.log(starSign(date))