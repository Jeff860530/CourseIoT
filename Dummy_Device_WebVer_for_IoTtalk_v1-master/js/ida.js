 $(function(){
        csmapi.set_endpoint ('https://6.iottalk.tw');
        var profile = {
		    'dm_name': 'Dummy_Device',          

			'odf_list':[L_0858611,C_0858611],
		        'd_name': undefined,
        };
		
        function Dummy_Sensor(){
            return Math.random();
        }

        function Dummy_Control(data){
           $('.ODF_value')[0].innerText = data[0];
        }
      
/*******************************************************************/                
        function ida_init(){
	    console.log(profile.d_name);
	}
        var ida = {
            'ida_init': ida_init,
        }; 
        dai(profile,ida);     
});
