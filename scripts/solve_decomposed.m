%% Solve using the decomposed method
function y = solve_decomposed(b)
global nbbus adf nbsync nbinj nbtwop bus_inj Bx By Ctx Cty LUDt LUA Dt A Tot_RHScorr_tmr Tot_RHSsol_tmr Tot_Injsol_tmr

bl = full(b); % KLU and PARDISO don't accept sparse RHS
RHScorr_tmr=tic;
for j=1:nbsync+nbinj+nbtwop
    i=bus_inj(j);
    shift=2*i-1;
    bl(shift)=bl(shift)-Cty{j}*bl(2*nbbus+adf(j):2*nbbus+adf(j+1)-1);
    bl(shift+1)=bl(shift+1)-Ctx{j}*bl(2*nbbus+adf(j):2*nbbus+adf(j+1)-1);
end
Tot_RHScorr_tmr=Tot_RHScorr_tmr+toc(RHScorr_tmr);
RHSsol_tmr=tic;
V = klu(LUDt,'\',bl(1:2*nbbus)) ;
% V= Dt \ bl(1:2*nbbus) ;
y = [V ; zeros(numel(bl)-2*nbbus,1)];
Tot_RHSsol_tmr=Tot_RHSsol_tmr+toc(RHSsol_tmr);

Injsol_tmr=tic;
for j=1:nbsync+nbinj+nbtwop
    i=bus_inj(j);
    for k=1:adf(j+1)-adf(j)
        bl(2*nbbus+adf(j)+k-1)=bl(2*nbbus+adf(j)+k-1)-Bx{j}(k)*V(2*i-1)-By{j}(k)*V(2*i);
    end
    y(2*nbbus+adf(j):2*nbbus+adf(j+1)-1,1) = klu(LUA{j},'\',bl(2*nbbus+adf(j):2*nbbus+adf(j+1)-1)) ;
%     y(2*nbbus+adf(j):2*nbbus+adf(j+1)-1,1) = A{j}\bl(2*nbbus+adf(j):2*nbbus+adf(j+1)-1) ;
end
Tot_Injsol_tmr=Tot_Injsol_tmr+toc(Injsol_tmr);
end