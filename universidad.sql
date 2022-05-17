-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-05-2022 a las 19:32:35
-- Versión del servidor: 10.4.22-MariaDB
-- Versión de PHP: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
USE universidad;
--
-- Base de datos: `universidad`
--

DELIMITER $$
--
-- Procedimientos
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `allDepartamentos` ()  BEGIN
	SELECT * FROM departamentos;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `allFinanciaciones` ()  BEGIN
	SELECT * FROM financiacion;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `allFuentes` ()  BEGIN
	SELECT * FROM fuentes;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `allProfesores` ()  BEGIN
	SELECT * FROM PROFESORES;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `allProgramas` ()  BEGIN
	SELECT * FROM programas;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `allProyectos` ()  BEGIN
	SELECT * FROM proyectos;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `createDepartamento` (`id` INT, `nombre` VARCHAR(45), `extension` VARCHAR(45), `jefe` INT)  BEGIN
	INSERT INTO departamentos VALUES (id, nombre, extension, jefe);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `createFinanciacion` (`idpro` INT, `idfue` INT, `monto` INT)  BEGIN
	INSERT INTO financiacion VALUES (idpro, idfue, monto);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `createFuente` (`id` INT, `nombre` VARCHAR(45), `direccion` VARCHAR(45), `telefono` VARCHAR(45))  BEGIN
	INSERT INTO fuentes VALUES (id, nombre, direccion, telefono);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `createPartiProy` (`prof` INT, `proy` INT, `Hora` DECIMAL(10,0))  BEGIN
	insert into participacion_proyecto values(prof,proy,Horas);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `createProyecto` (`id` INT, `nom` VARCHAR(45), `pre` INT, `fec` DATE, `lid` INT)  BEGIN
	INSERT INTO proyectos values(id,nom,pre,fec,lid);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteDepartamento` (`id` INT)  BEGIN
	DELETE FROM departamentos WHERE idDepartamentos = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteFinanciacion` (`idpro` INT, `idfue` INT)  BEGIN
	DELETE FROM financiacion WHERE idProyecto = idpro AND idFuente = idfue;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteFuente` (`id` INT)  BEGIN
	DELETE FROM fuentes WHERE idFuente = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `deletePartiProy` (`prof` INT, `proy` INT)  BEGIN
	DELETE FROM participacion_proyecto WHERE idProfesor=prof and idProyecto=proy;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteProfesor` (`id` INT)  BEGIN
	DELETE FROM PROFESORES WHERE idProfesor=id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `deletePrograma` (`id` INT)  BEGIN
	DELETE FROM PROGRAMAS WHERE idProgramas=id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `deleteProyecto` (`id` INT)  BEGIN
	DELETE FROM proyectos WHERE idProyectos = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getAllPartiProy` ()  BEGIN
	select profesores.Nombre,proyectos.Nombre,Horas from participacion_proyecto 
    inner join profesores on profesores.idProfesor = participacion_proyecto.idProfesor 
    inner join proyectos on proyectos.idProyectos = participacion_proyecto.idProyecto;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getDepartamento` (`id` INT)  BEGIN
	SELECT * FROM departamentos WHERE idDepartamentos = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getFinanciacion` (`idpro` INT, `idfue` INT)  BEGIN
	SELECT * FROM financiacion WHERE idProyecto = idpro AND idFuente = idfue;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getFuentes` (`id` INT)  BEGIN
	SELECT * FROM fuentes WHERE idFuente = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getProfesor` (`id` INT)  BEGIN
	SELECT * FROM PROFESORES WHERE idProfesor=id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getPrograma` (`id` INT)  BEGIN
	SELECT * FROM PROGRAMAS WHERE idProgramas = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `getProyecto` (`id` INT)  BEGIN
		SELECT * FROM proyectos WHERE idProyectos = id;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `insertProfesor` (`ID` INT, `NOMBRE` VARCHAR(100), `DIRECCION` VARCHAR(80), `TELEFONO` VARCHAR(20), `PROGRAMA` INT)  BEGIN
	INSERT INTO PROFESORES VALUES (ID, NOMBRE, DIRECCION, TELEFONO, PROGRAMA);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `insertPrograma` (`id` INT, `nombre` VARCHAR(45), `telefono` VARCHAR(45), `director` INT, `departamento` INT)  BEGIN
	INSERT INTO programas VALUES (id, nombre, telefono, director, departamento);
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `searchPartiProy` (`prof` INT, `proy` INT)  BEGIN
	select * from participacion_proyecto where idProfesor =prof and idProyecto = proy;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updateDepartamento` (`id` INT, `nombre` VARCHAR(45), `extension` VARCHAR(45), `jefe` INT, `idToUpdate` INT)  BEGIN
	UPDATE departamentos 
    SET 
    idDepartamentos = id,
    Nombre= nombre,
    Extension = extension,
    Jefe = jefe
    Where idDepartamentos = idToUpdate;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updateFinanciacion` (`idPNuevo` INT, `idFNuevo` INT, `monto` INT, `idPViejo` INT, `idFViejo` INT)  BEGIN
	UPDATE Financiacion SET idProyecto=idPNuevo, idFuente=idFNuevo,Monto=monto
	WHERE idProyecto=idPViejo AND idFuente=idFViejo;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updateFuente` (`id` INT, `nombre` VARCHAR(45), `direccion` VARCHAR(45), `telefono` VARCHAR(45), `idToUpdate` INT)  BEGIN
	UPDATE fuentes
    SET 
    idFuente = id,
    Nombre = nombre,
    Direccion = direccion,
    Telefono = telefono
    WHERE idFuente = idToUpdate;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updatePartiProy` (`prof` INT, `proy` INT, `horas` DECIMAL, `oldprof` INT, `oldproy` INT)  BEGIN
	update participacion_proyecto set idProfesor = prof, idProyecto = proy, Horas = horas
    where idProfesor = oldprof and idProyecto = oldproy;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updateProfesor` (`idAct` INT, `ID` INT, `NOMBRE` VARCHAR(100), `DIRECCION` VARCHAR(80), `TELEFONO` VARCHAR(20), `PROGRAMA` INT)  BEGIN
	UPDATE PROFESORES SET idProfesor=ID, Nombre=NOMBRE, Direccion=DIRECCION, Telefono=TELEFONO, Programa=PROGRAMA WHERE idProfesor=idAct;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updatePrograma` (`idAct` INT, `id` INT, `nombre` VARCHAR(45), `telefono` VARCHAR(45), `director` INT, `departamento` INT)  BEGIN
	UPDATE PROGRAMAS SET idProgramas=id, Nombre=nombre, Telefono=telefono, Director=director, Departamento=departamento WHERE idProgramas=idAct;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `updateProyecto` (`id` INT, `oldid` INT, `nom` VARCHAR(45), `pre` INT, `fec` DATE, `lid` INT)  BEGIN
	UPDATE proyectos SET idProyectos=id, Nombre=nom, Presupuesto=pre, Fecha_inicio=fec, Lider=lid
    Where idProyectos = oldid;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `departamentos`
--

CREATE TABLE `departamentos` (
  `idDepartamentos` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Extension` varchar(45) DEFAULT NULL,
  `Jefe` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `departamentos`
--

INSERT INTO `departamentos` (`idDepartamentos`, `Nombre`, `Extension`, `Jefe`) VALUES
(1, 'Depto 1', '2501', 3),
(2, 'calculo', '2502', 1),
(3, 'contabilidad', '798456', 1),
(4, 'ingenieria', '789456132', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `financiacion`
--

CREATE TABLE `financiacion` (
  `idProyecto` int(11) NOT NULL,
  `idFuente` int(11) NOT NULL,
  `Monto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `financiacion`
--

INSERT INTO `financiacion` (`idProyecto`, `idFuente`, `Monto`) VALUES
(1, 2, 200000),
(1, 4, 800000),
(3, 5, 99);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `fuentes`
--

CREATE TABLE `fuentes` (
  `idFuente` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Direccion` varchar(45) NOT NULL,
  `Telefono` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `fuentes`
--

INSERT INTO `fuentes` (`idFuente`, `Nombre`, `Direccion`, `Telefono`) VALUES
(1, 'Icetex', 'calle 8 # 2-57', '8526666'),
(2, 'Bancolombia', 'av 19 # 151-80', '2113232'),
(3, 'nequi', 'calle 54', '8521563'),
(4, 'DAVIPLATA', 'calle 5 #11-11', '7894562'),
(5, 'av villas ', 'calle 56', '798456');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `participacion_proyecto`
--

CREATE TABLE `participacion_proyecto` (
  `idProfesor` int(11) NOT NULL,
  `idProyecto` int(11) NOT NULL,
  `Horas` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `participacion_proyecto`
--

INSERT INTO `participacion_proyecto` (`idProfesor`, `idProyecto`, `Horas`) VALUES
(1, 2, 2),
(2, 1, 10);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `profesores`
--

CREATE TABLE `profesores` (
  `idProfesor` int(11) NOT NULL,
  `Nombre` varchar(100) NOT NULL,
  `Direccion` varchar(80) NOT NULL,
  `Telefono` varchar(20) NOT NULL,
  `Programa` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `profesores`
--

INSERT INTO `profesores` (`idProfesor`, `Nombre`, `Direccion`, `Telefono`, `Programa`) VALUES
(1, 'vale', 'calle 98', '7945163', 1),
(2, 'julian ', 'calle 5', '789456', 1),
(3, 'ana ', 'calle 78', '3165334569', 1),
(4, 'luis beltran ', 'calle 9 # 2-27', '3196034036', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `programas`
--

CREATE TABLE `programas` (
  `idProgramas` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Telefono` varchar(45) NOT NULL,
  `Director` int(11) DEFAULT NULL,
  `Departamento` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `programas`
--

INSERT INTO `programas` (`idProgramas`, `Nombre`, `Telefono`, `Director`, `Departamento`) VALUES
(1, 'informatica', '7778', 1, 1),
(2, 'mecanica', '132564', 1, 2),
(3, 'Ingenieria Industrial', '8521563', 2, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proyectos`
--

CREATE TABLE `proyectos` (
  `idProyectos` int(11) NOT NULL,
  `Nombre` varchar(45) NOT NULL,
  `Presupuesto` int(11) NOT NULL,
  `Fecha_inicio` date NOT NULL,
  `Lider` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `proyectos`
--

INSERT INTO `proyectos` (`idProyectos`, `Nombre`, `Presupuesto`, `Fecha_inicio`, `Lider`) VALUES
(1, 'siga', 2000000, '0000-00-00', 4),
(2, 'app unisabana', 3000000, '2020-06-12', 2),
(3, 'Exodo', 750000, '2022-05-11', 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD PRIMARY KEY (`idDepartamentos`),
  ADD KEY `fk_jefe_departamento` (`Jefe`);

--
-- Indices de la tabla `financiacion`
--
ALTER TABLE `financiacion`
  ADD PRIMARY KEY (`idProyecto`,`idFuente`),
  ADD KEY `fk_fin_fuente` (`idFuente`);

--
-- Indices de la tabla `fuentes`
--
ALTER TABLE `fuentes`
  ADD PRIMARY KEY (`idFuente`);

--
-- Indices de la tabla `participacion_proyecto`
--
ALTER TABLE `participacion_proyecto`
  ADD PRIMARY KEY (`idProfesor`,`idProyecto`),
  ADD KEY `fk_proyecto` (`idProyecto`);

--
-- Indices de la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD PRIMARY KEY (`idProfesor`),
  ADD KEY `fk_programa_profesor` (`Programa`);

--
-- Indices de la tabla `programas`
--
ALTER TABLE `programas`
  ADD PRIMARY KEY (`idProgramas`),
  ADD KEY `fk_director_programa` (`Director`),
  ADD KEY `fk_departamento_programa` (`Departamento`);

--
-- Indices de la tabla `proyectos`
--
ALTER TABLE `proyectos`
  ADD PRIMARY KEY (`idProyectos`),
  ADD KEY `fk_lider_proyecto` (`Lider`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `profesores`
--
ALTER TABLE `profesores`
  MODIFY `idProfesor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `departamentos`
--
ALTER TABLE `departamentos`
  ADD CONSTRAINT `fk_jefe_departamento` FOREIGN KEY (`Jefe`) REFERENCES `profesores` (`idProfesor`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Filtros para la tabla `financiacion`
--
ALTER TABLE `financiacion`
  ADD CONSTRAINT `fk_fin_fuente` FOREIGN KEY (`idFuente`) REFERENCES `fuentes` (`idFuente`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_fin_proyecto` FOREIGN KEY (`idProyecto`) REFERENCES `proyectos` (`idProyectos`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `participacion_proyecto`
--
ALTER TABLE `participacion_proyecto`
  ADD CONSTRAINT `fk_profesor` FOREIGN KEY (`idProfesor`) REFERENCES `profesores` (`idProfesor`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_proyecto` FOREIGN KEY (`idProyecto`) REFERENCES `proyectos` (`idProyectos`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `profesores`
--
ALTER TABLE `profesores`
  ADD CONSTRAINT `fk_programa_profesor` FOREIGN KEY (`Programa`) REFERENCES `programas` (`idProgramas`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Filtros para la tabla `programas`
--
ALTER TABLE `programas`
  ADD CONSTRAINT `fk_departamento_programa` FOREIGN KEY (`Departamento`) REFERENCES `departamentos` (`idDepartamentos`) ON DELETE SET NULL ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_director_programa` FOREIGN KEY (`Director`) REFERENCES `profesores` (`idProfesor`) ON DELETE SET NULL ON UPDATE CASCADE;

--
-- Filtros para la tabla `proyectos`
--
ALTER TABLE `proyectos`
  ADD CONSTRAINT `fk_lider_proyecto` FOREIGN KEY (`Lider`) REFERENCES `profesores` (`idProfesor`) ON DELETE SET NULL ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
