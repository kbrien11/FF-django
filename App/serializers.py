from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Quarterback,Runningback,Widereceiver,Tightend,Defense,Kicker,Player

class QuarterbacksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quarterback
        fields = ['id','name','team','position','Bye_Week','Passing_yards','Passing_TD','INT','Rush_Yards','Rush_TD','FPTS','Projected_Passing_yards','Projected_Passing_TD',
                  'Projected_INT','Projected_Rush_Yards','Projected_Rush_TD','Projected_FPTS','Projected_OUTLOOK']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password','email','first_name','last_name']
        extra_kwargs = {'password':{'write_only':True,'required':True}}

    def create(self,validated_data):
            user = User.objects.create_user(**validated_data)
            Token.objects.create(user=user)
            return user

class RunningbackSerialier(serializers.ModelSerializer):
    class Meta:
        model = Runningback
        fields = ['id','name', 'team', 'position', 'bye_week', 'rush_yards', 'rush_td', 'receptions', 'rec_yards', 'rec_td',
                  'total_yards','total_td', 'fpts', 'projected_rush_yards', 'projected_rush_td',
                  'projected_receptions', 'projected_rec_yards', 'projected_rec_td','projected_total_yards'
                  ,'projected_total_td','projected_fpts', 'projected_OUTLOOK']

class WidereceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widereceiver
        fields = ['id','name', 'team', 'position', 'bye_week', 'targets', 'receptions', 'rec_yards', 'rec_td',
                   'fpts', 'projected_targets', 'projected_receptions','projected_rec_yards',
                  'projected_rec_td', 'projected_fpts', 'projected_OUTLOOK']

class TightendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tightend
        fields = ['id','name', 'team', 'position', 'bye_week', 'targets', 'receptions', 'rec_yards',
                  'rec_td',
                  'fpts', 'projected_targets', 'projected_receptions', 'projected_rec_yards',
                  'projected_rec_td', 'projected_fpts', 'projected_OUTLOOK']

class DefenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Defense
        fields = ['id','team','bye_week','sacks','turnovers','td','fpts','projected_sacks','projected_turnovers'
                  ,'projected_td','projected_fpts','projected_OUTLOOK']

class KickerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kicker
        fields = ['id','name','position','team','bye_week','total_made_fg','fpts','projected_total_made_fg',
                  'projected_fpts','projected_OUTLOOK']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['id','user','name','team','position','bye_week','is_drafted']


