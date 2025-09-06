function Angle = Quat_To_Yaw(quat)
    Quat = [quat(1,1), quat(2,1), quat(3,1), quat(4,1)];
    [~,~,yaw] = quat2angle(Quat,"YXZ");
    Angle =  yaw;
end