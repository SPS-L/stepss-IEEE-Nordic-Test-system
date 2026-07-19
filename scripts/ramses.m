function y = ramses(u)
global ram obsV comp_type comp_name obs_name tdel
% display(strcat('CHGPRM TOR g6 Tm0 ', num2str(u(2)/5.0), ' 0'));
% ram.addDisturb(ram.getSimTime() + tdel, strcat('CHGPRM TOR g6 Tm0 ', num2str(u(2)/5.0), ' 0'));
% ram.addDisturb(ram.getSimTime() + tdel, strcat('CHGPRM TOR g7 Tm0 ', num2str(u(2)/5.0), ' 0'));
% ram.addDisturb(ram.getSimTime() + tdel, strcat('CHGPRM TOR g14 Tm0 ', num2str(u(2)/5.0), ' 0'));
% ram.addDisturb(ram.getSimTime() + tdel, strcat('CHGPRM TOR g15 Tm0 ', num2str(u(2)/5.0), ' 0'));
% ram.addDisturb(ram.getSimTime() + tdel, strcat('CHGPRM TOR g16 Tm0 ', num2str(u(2)/5.0), ' 0'));
ram.contSim(u(1));
% y = ones(1, Nout) ;
y = [ cellfun(@double,cell(ram.getBusVolt(obsV))) cellfun(@double,cell(ram.getObs(comp_type,comp_name,obs_name))) u(2) ];

end




% comp_type = ['SYN']
% comp_name = ['g2']
% obs_name = ['Omega']
% errSum = 0.0
% t=500
% nominal_frequency = 1.0
% list_of_gens = ['g6', 'g7', 'g14', 'g15', 'g16']
% actual_frequency = ram.getObs(comp_type,comp_name, obs_name)[0]
% for gen in list_of_gens:
%     command = 'CHGPRM TOR ' + gen + ' Tm0 ' + str(output/5.0) + ' 0'
%     #print(str(ram.getSimTime()+0.01)+' '+command)
%     td = float(td)
%     ram.addDisturb(ram.getSimTime() + td, command)