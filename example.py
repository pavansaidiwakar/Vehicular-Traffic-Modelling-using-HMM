# -*- coding, utf-8 -*-

from hmm import Model
from hmm import train
sequences =  [(
	['2' ,'2' , '2' , '1' , '1' , '1' , '1' , '1' , '1' ,'1' , '1' , '1' ,  	#9AM
	 '1' , '1' , '1' , '1' , '1' , '1' , '1' , '2' , '2' , '2' , '2' , '2' ,	#10AM
	 '1' , '2' , '2' , '2' , '2' , '2' , '3' , '3' , '3' , '3' , '3' , '3' ,	#11AM
	 '3' , '3' , '3' , '4' , '4' , '4' , '5' , '5' , '5' , '4' , '4' , '4' ,	#12PM
	 '4' , '4' , '4' , '4' , '4' , 	'4' , '4' , '4' , '4' , '5' , '5' , '5' , 	#1PM
	 '5' , '5' , '5' , '5' , '5' , '4' , '4' , '5' , '5' , '5' , '5' , '5' ,	#2PM
	 '5' , '5' , '4' , '5' , '4' , '4' , '4' , '4' , '3' , '3' , '3' , '3' ,	#3PM
	 '3' , '3' , '2' , '2' , '2' ,'2' , '2' , '2' , '2' , '2' , '1' , '2' , 	#4PM
	 '1' , '1' , '1' , '1' , '2' , '2' , '1' , '1' , '1' , '1' , '1' , '1' ,	#5PM
	 '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '1' , '2' ,'2'], 	#6PM
	['MROO' , 'MROO' , 'MRRO' , 'MRRO'   , 'MRRO'   , 'MRRO'   , 'MRRO'   , 'MRRO'   , 'MRRO'   , 'MRRR'   , 'MRRR'   , 'MRRR'   , 'MMRO' 
	  , 'MRRO'   , 'RRRO'   , 'RRRO'   , 'MROO'   , 'MROO'   , 'MROG'   , 'MRGG'   , 'MROG'   , 'RROG'   , 'MROG'   , 'MROG'   , 'MRRO'   , 'MROO' 
	  , 'MOOO'   , 'RRRO'   , 'RRRO'   , 'RROO'   , 'RROO'   , 'RROG'   , 'RROG'   , 'ROOO'   , 'ROOO'   , 'RROG'   , 'ROOG'   , 'RRGG'   , 'MGGG' 
	  , 'RGGG'   , 'RGGG'   , 'ROGG'   , 'OOGG'   , 'OOGG'   , 'ROGG'   , 'ROOO'   , 'OOOO'   , 'OOOO'   , 'ROOO'   , 'ROOG'   , 'ROOG'   , 'ROGG' 
	  , 'RGGG'   , 'ROGG'   , 'OOOG'   , 'OOOG'   , 'OOOG'   , 'OOOG'   , 'OOOG'   , 'OOGG'   , 'OOGG'   , 'OGGG'   , 'GGGG'   , 'GGGG'   , 'OGGG' 
	  , 'RGGG'   , 'ROGG'   , 'OOOG'   , 'OOGG'   , 'OGGG'   , 'RGOG'   , 'OOGG'   , 'OOGG'   , 'OOOG'   , 'ROOG'   , 'ROOG'   , 'ROOG'   , 'ROGG' 
	  , 'OOOG'   , 'OOOO'   , 'OOOO'   , 'ROOO'   , 'ROOG'   , 'ROOO'   , 'RROG'   , 'RROO'   , 'MROO'   , 'MROO'   , 'MROG'   , 'MROG'   , 'MROO' 
	  , 'MMOO'   , 'MMOO'   , 'RRRO'   , 'RRRR'   , 'RRRR'   , 'MRRO'   , 'MRRO'   , 'MRRO'   , 'MMMR'   , 'MROO'   , 'MRRO'   , 'MRRO'   , 'MRRO' 
	  , 'MMOO'   , 'MMMO'   , 'MMMM'   , 'MMMM'   , 'MMMR'   , 'MRRR'   , 'MRRO'   , 'MROO'   , 'MROO'   , 'RRRO'   , 'MRRO'   , 'RRRO'   , 'MROO' 
	  , 'RROO'   , 'RROG'   , 'RROG'])]	
train(sequences)



