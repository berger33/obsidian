---
id: software.testes.tranche22.001589
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-22.md"
fontes: ["https://github.com/reqnroll/Reqnroll/blob/main/README.md", "https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# Reqnroll: por onde começar segundo o próprio projeto

## Em uma frase
O README oficial condensa o onboarding em rotas nomeadas: quickstart guide, site reqnroll.net, documentação em docs.reqnroll.net, página de configuração de projeto NuGet, instruções de IDE e release notes — cada uma apontando para o passo correspondente da adoção.

## Por que importa
Projetos BDD morrem no setup (gerador, runner, extension de IDE); o valor de seguir as rotas oficiais é que cada uma é mantida com a versão corrente do Reqnroll, sem tutorial desatualizado.

## Como funciona
Siga a rota de setup de projeto para instalar o pacote Reqnroll.NUnit/MsTest/xUnit/TUnit adequado e as instruções de IDE para habilitar highlighting e runner no seu editor.

## Exemplo
O link "project setup documentation page" no README é a continuação obrigatória depois de escolher o pacote — é onde a documentação detalha as opções de generator.

## Limites e trade-offs
Rotas "go.reqnroll.net" são redirecionadores mantidos à parte; conferir neles o destino final evita depender de atalho quebrado anos depois.

## Como verificar
Execute o quickstart numa pasta vazia com dotnet SDK instalado e confirme que o projeto gerado roda sem ajuste manual de csproj.

## Conexões
- [[reqnroll-license-sponsors]] — Veja também: Reqnroll: licença, patrocínio e linhagem.

## Fontes
- [Reqnroll — README oficial](https://github.com/reqnroll/Reqnroll/blob/main/README.md) — proposta, plataformas, executores e instalação NuGet; consultado em 2026-10-03.
- [Reqnroll — Migrating from SpecFlow](https://docs.reqnroll.net/latest/guides/migrating-from-specflow.html) — renomeações, compat package, atenções MsTest e LivingDoc; consultado em 2026-10-03.
