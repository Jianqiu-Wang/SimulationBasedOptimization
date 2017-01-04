%% Simulation Benchmark
% A simple graph: 2 nodes only: 1 supplier and 1 customer
%% Pass parameter to simulator


k = 1;
N0 = 100; % warm up horizon
N1 = 200; % data collection horizon
Nd = N0 + N1; % total simulation horizon
%n1 = zeros(N,1); % node 1
%n4 = normrnd(150,30,[N,1]); % node 4

%% Inventory system simulation
t = 0;

% Inventory operations
while (t < Nd)
    % Place order
    
    t = t + 1;
end

% Calculating performances

%% Return result
% Totoal daily opertion cost
% Service level for each inventory node