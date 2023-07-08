
Select * 
From Portfolio..CovidDeaths
Where continent is not null
Order by 3, 4

--Select * 
--From Portfolio..CovidVaccinations
--Order by 3, 4

-- Select the data that we are going to be using.
Select location, date, total_cases, new_cases, total_deaths, population
From Portfolio..CovidDeaths
Where continent is not null
Order by 1, 2

-- Total Cases vs Total Deaths 
-- Shows the likelihood of dying if you contract covid

Select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathPercentage
From Portfolio..CovidDeaths
Where location like 'Pakistan'
Order by 1, 2

-- Total Cases vs Population
-- Shows what percentage of population got covid
Select location, date, total_cases, population, (total_cases/population)*100 as PercentPopulationInfected
From Portfolio..CovidDeaths
Where location like 'Pakistan'
Order by 1, 2

-- Countries with Highest Infection Rate compared to Population
Select location, population, MAX(total_cases) as HighestInfectionCount, MAX((total_cases/population))*100 as PercentPopulationInfected
From Portfolio..CovidDeaths
Group by location, population
Order by PercentPopulationInfected desc

-- Countries with the Highest Death Count per Population
Select location,  MAX(cast(total_deaths as int)) as TotalDeathCount
From Portfolio..CovidDeaths
Where continent is not null
Group by location
Order by TotalDeathCount desc

-- Continents with the Highest Death Count
Select location,  MAX(cast(total_deaths as int)) as TotalDeathCount
From Portfolio..CovidDeaths
Where continent is null
Group by location
Order by TotalDeathCount desc

-- Global Numbers
Select  date, SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100 as DeathPercentage
From Portfolio..CovidDeaths
Where continent is not null
Group by date
Order by 1, 2

-- Entire World Combined
Select SUM(new_cases) as total_cases, SUM(cast(new_deaths as int)) as total_deaths, SUM(cast(new_deaths as int))/SUM(new_cases)*100 as DeathPercentage
From Portfolio..CovidDeaths
Where continent is not null
Order by 1, 2



-- Total Population vs Vaccinations
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(convert(int, vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location
, dea.date) as RollingPeopleVaccinated--, (RollingPeopleVaccinated/population)*100
From Portfolio..CovidDeaths dea
Join Portfolio..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
Where dea.continent is not null
Order by 2,3


-- Using CTE
With PopvsVac (Continent, Location, Date, Population,New_Vaccinations, RollingPeopleVaccinated)
as
(
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(convert(int, vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location
, dea.date) as RollingPeopleVaccinated
From Portfolio..CovidDeaths dea
Join Portfolio..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
Where dea.continent is not null
--Order by 2,3
)

Select * , (RollingPeopleVaccinated / Population)*100
From PopvsVac

-- Temp Table
Drop Table if exists #PercentPopulationVaccinated
Create Table #PercentPopulationVaccinated
(
Continent nvarchar(255),
Location nvarchar(255),
Date datetime,
Population numeric,
New_vaccinations numeric,
RollingPeopleVaccinated numeric
)

Insert Into #PercentPopulationVaccinated
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(convert(int, vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location
, dea.date) as RollingPeopleVaccinated--, (RollingPeopleVaccinated/population)*100
From Portfolio..CovidDeaths dea
Join Portfolio..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
--Where dea.continent is not null
Order by 2,3

Select * , (RollingPeopleVaccinated / Population)*100
From #PercentPopulationVaccinated

-- Creating View to store data for later visualizations
Create View PercentPopulationVaccinated as
Select dea.continent, dea.location, dea.date, dea.population, vac.new_vaccinations
, SUM(convert(int, vac.new_vaccinations)) OVER (Partition by dea.location Order by dea.location
, dea.date) as RollingPeopleVaccinated
From Portfolio..CovidDeaths dea
Join Portfolio..CovidVaccinations vac
	On dea.location = vac.location
	and dea.date = vac.date
Where dea.continent is not null
--Order by 2,3

Select *
From PercentPopulationVaccinated





