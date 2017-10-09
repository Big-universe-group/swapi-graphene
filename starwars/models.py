# coding:utf8
# Models and fixtures taked from Swapi
# Swapi URL project: https://github.com/phalt/swapi/
# https://github.com/phalt/swapi/blob/master/resources/models.py
from __future__ import unicode_literals

from django.db import models


class DateTimeModel(models.Model):
    """ A base model with created and edited datetime fields """

    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Planet(DateTimeModel):
    """ A planet i.e. Tatooine 星球-星球大战"""

    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True)
    rotation_period = models.CharField(max_length=40)  # 旋转周期
    orbital_period = models.CharField(max_length=40)  # 轨道周期
    diameter = models.CharField(max_length=40)  # 星球直径
    climate = models.CharField(max_length=40)  # 气候
    gravity = models.CharField(max_length=40)  # 重力
    terrain = models.CharField(max_length=40)  # 地形
    surface_water = models.CharField(max_length=40)  # 地表水资源
    population = models.CharField(max_length=40)  # 人口数量

    def __unicode__(self):
        return self.name


class People(DateTimeModel):
    """ A person i.e. - Luke Skywalker """

    name = models.CharField(max_length=100)
    height = models.CharField(max_length=10, blank=True)
    mass = models.CharField(max_length=10, blank=True)  # 质量
    hair_color = models.CharField(max_length=20, blank=True)  # 发色
    skin_color = models.CharField(max_length=20, blank=True)  # 肤色
    eye_color = models.CharField(max_length=20, blank=True)  # 眼睛
    birth_year = models.CharField(max_length=10, blank=True)  # 出生年份
    gender = models.CharField(max_length=40, blank=True)  # 性别
    homeworld = models.ForeignKey(Planet, related_name="residents")  # 所属星球

    def __unicode__(self):
        return self.name


class Transport(DateTimeModel):
    """飞行器"""

    name = models.CharField(max_length=40)
    model = models.CharField(max_length=40)  # 模型
    manufacturer = models.CharField(max_length=80)  # 制造商
    cost_in_credits = models.CharField(max_length=40)  # 成本额度
    length = models.CharField(max_length=40)  # 长度
    max_atmosphering_speed = models.CharField(max_length=40)  # 大气中的飞行速度
    crew = models.CharField(max_length=40)  # 机组成员
    passengers = models.CharField(max_length=40)  # 乘客
    cargo_capacity = models.CharField(max_length=40)  # 载货能力
    consumables = models.CharField(max_length=40)  # 耗材

    def __unicode__(self):
        return self.name


class Starship(Transport):
    """ A starship is a transport with a hypderdrive(超光速) """

    hyperdrive_rating = models.CharField(max_length=40)  # 超光速推进速率
    MGLT = models.CharField(max_length=40)  # 速度单位
    starship_class = models.CharField(max_length=40)  # 星际飞船作战序列
    pilots = models.ManyToManyField(  # 飞行员
        People,
        related_name="starships",
        blank=True
    )


class Vehicle(Transport):
    """ A vehicle(交通工具) is anything without hyperdrive capability """

    vehicle_class = models.CharField(max_length=40)  # 类型
    pilots = models.ManyToManyField(  # 飞行员
        People,
        related_name="vehicles",
        blank=True
    )


class Species(DateTimeModel):
    "A species-生物,物种 is a type of alien-外星人 or person"

    name = models.CharField(max_length=40)
    classification = models.CharField(max_length=40)  # 分类
    designation = models.CharField(max_length=40)  # 名称, 任命, 指示
    average_height = models.CharField(max_length=40)  # 平均身高
    skin_colors = models.CharField(max_length=200)  # 肤色
    hair_colors = models.CharField(max_length=200)  # 发色
    eye_colors = models.CharField(max_length=200)  # 眼睛
    average_lifespan = models.CharField(max_length=40)  # 平均寿命
    homeworld = models.ForeignKey(Planet, blank=True, null=True)  # 所属星系
    language = models.CharField(max_length=40)  # 语言
    people = models.ManyToManyField(People, related_name="species")

    def __unicode__(self):
        return self.name


class Film(DateTimeModel):
    """ A film i.e. The Empire Strikes Back-帝国反击战 (which is also the best film) """

    title = models.CharField(max_length=100)  # 电影名
    episode_id = models.IntegerField()  # 插曲, 故事情节
    opening_crawl = models.TextField(max_length=1000)  # 
    director = models.CharField(max_length=100)  # 导演
    producer = models.CharField(max_length=100)  # 制片人
    release_date = models.DateField()  # 定档日期
    characters = models.ManyToManyField(  # 参演人员
        People,
        related_name="films",
        blank=True
    )
    planets = models.ManyToManyField(  # 星系
        Planet,
        related_name="films",
        blank=True
    )
    starships = models.ManyToManyField(  # 飞行器
        Starship,
        related_name="films",
        blank=True
    )
    vehicles = models.ManyToManyField(  # 交通工具
        Vehicle,
        related_name="films",
        blank=True
    )
    species = models.ManyToManyField(  # 物种
        Species,
        related_name="films",
        blank=True
    )

    def __unicode__(self):
        return self.title


class Hero(DateTimeModel):
    """英雄, 主角"""
    name = models.CharField(max_length=100)
    homeworld = models.ForeignKey(Planet, related_name="heroes")  # 所属星系
