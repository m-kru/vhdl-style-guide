
architecture ARCH of ENTITY_1 is

  function func_1 (a : integer) return integer is
  begin

    if (a > 2) then
      return 6;
    else
      return 0;
    end if;

  end;


 function func_1 (a : integer) return integer is
   begin
     return 10;
 end;
   -- A comment above a function is okay, but not after the end
   function func_1 (a : integer) return integer is
 begin
 return 11;
   end;
  signal a : std_logic;

  
  function func_1 (a : integer
                   b : integer
                  ) return integer is
  begin

  end;


  function func_1 (a : integer) return integer is
  begin

    case A is
      when 0 =>
      when 1 =>
      when others =>
    end case;

  end;


begin


end architecture ARCH;