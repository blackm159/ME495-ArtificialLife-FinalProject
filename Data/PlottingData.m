%% Start

% Close all open plots, clear all variables, and clear the command window log
close all
clear all
clc

%% Define Dataset

coev{1}  = readmatrix("CoEvolution_seed1.txt");
brain{1}  = readmatrix("BrainBody_seed1.txt");
body{1}  = readmatrix("BodyBrain_seed1.txt");
prob{1}  = readmatrix("Probability_seed1.txt");

coev{2}  = readmatrix("CoEvolution_seed3.txt");
brain{2}  = readmatrix("BrainBody_seed3.txt");
body{2}  = readmatrix("BodyBrain_seed3.txt");
prob{2}  = readmatrix("Probability_seed3.txt");

coev{3}  = readmatrix("CoEvolution_seed4.txt");
brain{3}  = readmatrix("BrainBody_seed4.txt");
body{3}  = readmatrix("BodyBrain_seed4.txt");
prob{3}  = readmatrix("Probability_seed4.txt");

coev{4}  = readmatrix("CoEvolution_seed25.txt");
brain{4}  = readmatrix("BrainBody_seed25.txt");
body{4}  = readmatrix("BodyBrain_seed25.txt");
prob{4}  = readmatrix("Probability_seed25.txt");

coev{5}  = readmatrix("CoEvolution_seed100.txt");
brain{5}  = readmatrix("BrainBody_seed100.txt");
body{5}  = readmatrix("BodyBrain_seed100.txt");
prob{5}  = readmatrix("Probability_seed100.txt");


gen = 0:length(coev{1})-1;

%% Average

coev_avg = 0*gen;
for ind = 1:length(coev)
    coev_avg = coev_avg + coev{ind};
end
coev_avg = coev_avg/ind;


brain_avg = 0*gen;
for ind = 1:length(brain)
    brain_avg = brain_avg + brain{ind};
end
brain_avg = brain_avg/ind;


body_avg = 0*gen;
for ind = 1:length(body)
    body_avg = body_avg + body{ind};
end
body_avg = body_avg/ind;


prob_avg = 0*gen;
for ind = 1:length(prob)
    prob_avg = prob_avg + prob{ind};
end
prob_avg = prob_avg/ind;


%% Plot Average

figure()
plot(gen, -1*coev_avg, 'b', 'LineWidth', 2)
hold on
plot(gen, -1*brain_avg, 'r', 'LineWidth', 2)
hold on
plot(gen, -1*body_avg, 'k', 'LineWidth', 2)
hold on
plot(gen, -1*prob_avg, 'g', 'LineWidth', 2)

legend("CoEvolution", "Brain First", "Body First", "Probability", 'Location', 'southeast')
title("Average Fitness vs. Generation")
xlabel("Generation")
ylabel("Fitness (-y units)")
% xlim([0, length(gen)-1])


%% Plot All

figure()
plot(gen, -1*coev_avg, 'b', 'LineWidth', 2)
hold on
plot(gen, -1*brain_avg, 'r', 'LineWidth', 2)
hold on
plot(gen, -1*body_avg, 'k', 'LineWidth', 2)
hold on
plot(gen, -1*prob_avg, 'g', 'LineWidth', 2)

for ind = 1:length(coev)
    hold on
    plot(gen, -1*coev{ind}, 'b', 'LineWidth', 1)
    hold on
    plot(gen, -1*brain{ind}, 'r', 'LineWidth', 1)
    hold on
    plot(gen, -1*body{ind}, 'k', 'LineWidth', 1)
    hold on
    plot(gen, -1*prob{ind}, 'g', 'LineWidth', 1)
end


legend("CoEvolution", "Brain First", "Body First", "Probability", 'Location', 'southeast')
title("Fitness vs. Generation")
xlabel("Generation")
ylabel("Fitness (-y units)")
% xlim([0, length(gen)-1])


%% Plot All

figure()
subplot(2,2,1)
title("Co-Evolution")
plot(gen, -1*coev_avg, 'b', 'LineWidth', 2)
hold on

for ind = 1:length(coev)
    hold on
    plot(gen, -1*coev{ind}, 'b', 'LineWidth', 1)
end

subplot(2,2,1)
title("Co-Evolution")
plot(gen, -1*coev_avg, 'b', 'LineWidth', 2)
hold on

for ind = 1:length(coev)
    hold on
    plot(gen, -1*coev{ind}, 'b', 'LineWidth', 1)
end


plot(gen, -1*brain_avg, 'r', 'LineWidth', 2)
hold on
plot(gen, -1*body_avg, 'k', 'LineWidth', 2)
hold on
plot(gen, -1*prob_avg, 'g', 'LineWidth', 2)


for ind = 1:length(coev)
    hold on
    plot(gen, -1*coev{ind}, 'b', 'LineWidth', 1)
    hold on
    plot(gen, -1*brain{ind}, 'r', 'LineWidth', 1)
    hold on
    plot(gen, -1*body{ind}, 'k', 'LineWidth', 1)
    hold on
    plot(gen, -1*prob{ind}, 'g', 'LineWidth', 1)
end

% legend("CoEvolution", "Brain First", "Body First", "Probability", 'Location', 'southeast')
% title("Fitness vs. Generation")
% xlabel("Generation")
% ylabel("Fitness (-y units)")
% % xlim([0, length(gen)-1])
