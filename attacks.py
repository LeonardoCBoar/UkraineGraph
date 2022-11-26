import copy
import random

import networkx

import metrics


def attack_city(ukraine: networkx.Graph, city_list: list, target_city: int) -> metrics.Metrics:

    after_attack_ukraine = copy.deepcopy(ukraine)
    after_attack_ukraine.remove_node(target_city)
    after_attack_city_list = copy.deepcopy(city_list)
    after_attack_city_list.remove(target_city)
    after_attack_metrics = metrics.calculate_metrics(after_attack_ukraine, after_attack_city_list)

    return after_attack_metrics


def attack_path(ukraine: networkx.Graph, city_list: list, target_path: list) -> metrics.Metrics:

    origin = target_path[0]
    target = target_path[1]
    after_attack_ukraine = copy.deepcopy(ukraine)
    after_attack_ukraine.remove_edge(origin, target)
    after_attack_metrics = metrics.calculate_metrics(after_attack_ukraine, city_list)

    return after_attack_metrics


def attack_random_city(ukraine: networkx.Graph, city_list: list):

    target_city = random.choice(city_list)
    city_list.remove(target_city)
    ukraine.remove_node(target_city)


def attack_random_path(ukraine: networkx.Graph, path_list: list):
    
    target_path = random.choice(path_list)
    origin_city = target_path[0]
    target_city = target_path[1]
    path_list.remove(target_path)

    ukraine.remove_edge(origin_city, target_city)
