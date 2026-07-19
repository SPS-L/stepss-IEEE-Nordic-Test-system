function y = ramses_init(u)
global ram obsV comp_type comp_name obs_name tdel Nout

obsV = py.list({'4032', '1041'});
comp_type = py.list({'SYN'});
comp_name = py.list({'g2'});
obs_name = py.list({'Omega'});
tdel = 0.01;
Nout = 4;

try
    ram.endSim()
catch
    
end

clear ram
import py.PyRAMSES.*
ram = py.PyRAMSES.sim();
caseR = py.PyRAMSES.cfg("cmd.txt");
ram.execSim(caseR,0);
y = ones(1, Nout) ;

end