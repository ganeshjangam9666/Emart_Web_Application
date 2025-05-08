var op=data.price
var dis=data.discount
var price=op-(op*dis/100)
document.getElementById("amount").innerHTML = <p>"₹"+price+" M.R.P: ₹"+op+" ("+dis+"%)"</p>;