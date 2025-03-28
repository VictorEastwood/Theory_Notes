function Angle = Quat_To_Pitch(quat)
    Quat = [quat(1,1), quat(2,1), quat(3,1), quat(4,1)];
    [pitch,~,~] = quat2angle(Quat,"YXZ");
    Angle =  pitch;
end