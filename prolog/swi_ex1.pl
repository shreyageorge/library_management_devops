% ==========================================
% SMART AQUARIUM KNOWLEDGE REPRESENTATION
% ==========================================

% -------- Fish --------

fish(goldie).
fish(nemo).
fish(dory).

% -------- Tanks --------

tank(freshwater_tank).

% -------- Fish living in tanks --------

lives_in(goldie, freshwater_tank).
lives_in(nemo, freshwater_tank).
lives_in(dory, freshwater_tank).

% -------- Food --------

eats(goldie, flakes).
eats(nemo, pellets).
eats(dory, flakes).

% -------- Aquarium equipment --------

has_filter(freshwater_tank).
has_heater(freshwater_tank).

% -------- Water requirement --------

requires_clean_water(goldie).
requires_clean_water(nemo).
requires_clean_water(dory).

% ==========================================
% RULES
% ==========================================

% A fish requires clean water.

requires_clean_water_for_fish(Fish) :-
    fish(Fish).

% A fish is healthy if it has access to
% clean water.

healthy(Fish) :-
    fish(Fish),
    requires_clean_water(Fish).

% A fish requires a heater if it lives
% in a tank that has a heater.

requires_heater(Fish) :-
    fish(Fish),
    lives_in(Fish, Tank),
    has_heater(Tank).

% A fish requires filtration if it lives
% in a tank that has a filter.

requires_filtration(Fish) :-
    fish(Fish),
    lives_in(Fish, Tank),
    has_filter(Tank).

% A fish is well maintained if it has
% clean water, heating, and filtration.

well_maintained(Fish) :-
    fish(Fish),
    requires_clean_water(Fish),
    requires_heater(Fish),
    requires_filtration(Fish).
