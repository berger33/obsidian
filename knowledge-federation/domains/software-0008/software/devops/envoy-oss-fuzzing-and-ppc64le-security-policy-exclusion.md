---
id: software.devops.tranche03.000279
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-03.md"
fontes: ["https://raw.githubusercontent.com/envoyproxy/envoy/main/README.md", "https://github.com/envoyproxy/envoy"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Integração contínua com OSS-Fuzz e exclusão da arquitetura ppc64le da política de segurança

## Em uma frase
As subseções `OSS fuzzing`, `ppc64le builds` e `Other builds` na seção `Security` do README mostram o status de fuzzing contínuo do projeto no Google **OSS-Fuzz** (`proj:envoy`), os pipelines de CI para `ppc64le` e `s390x` no OSUOSL e um aviso de segurança crucial: **builds para a arquitetura `ppc64le` não são cobertas pela política de segurança do Envoy** (`Builds for the ppc64le architecture are not covered by the envoy security policy`), sendo mantidas apenas em regime de melhor esforço (`best-effort`) e não mantidas pelos mantenedores oficiais do Envoy.

## Por que importa
Organizações que operam servidores IBM Power (`ppc64le`) precisam estar cientes dessa exclusão explícita na política de segurança do projeto antes de expor binários Envoy `ppc64le` em fronteiras críticas de rede.

## Como funciona
Para cargas críticas sujeitas a requisitos formais de cobertura da política de segurança do Envoy, implante o Envoy nas arquiteturas oficialmente suportadas e cobertas pelos mantenedores, evitando depender de builds `ppc64le` best-effort na borda pública.

## Exemplo
Ao revisar a matriz de arquiteturas aprovadas para o gateway corporativo, o arquiteto registra a restrição documentada no README sobre `ppc64le` e padroniza os nós de borda em arquiteturas cobertas pela política de segurança.

## Limites e trade-offs
Verifique sempre a cobertura de suporte de arquitetura em `SECURITY.md` e `RELEASES.md` antes de adotar plataformas de hardware não convencionais.

## Como verificar
Conferi as subseções OSS fuzzing, ppc64le builds e Other builds no README oficial de envoyproxy/envoy.

## Conexões
- [[envoy-vulnerability-reporting-and-security-release-process]] — Veja também: Canal preferencial de relato de vulnerabilidades via GitHub Security Advisory e SECURITY.md.
- [[envoy-release-process-and-lifecycle-governance]] — Veja também: Processo formal de lançamento e governança de versões em RELEASES.md.

## Fontes
- [Envoy Proxy — GitHub README](https://raw.githubusercontent.com/envoyproxy/envoy/main/README.md) — Visão geral do Envoy (edge/middle/service proxy na CNCF, artigos de arquitetura sobre threading, hot restart, stats e xDS, repositórios relacionados, listas de e-mail, reuniões, auditorias Cure53/Ada Logics, OSS-Fuzz e política ppc64le).; consultado em 2026-10-03.
- [Envoy Proxy — Repositório Oficial no GitHub](https://github.com/envoyproxy/envoy) — Repositório oficial do Envoy Proxy com código-fonte C++, api/, docs/security/, DEVELOPER.md, SECURITY.md e RELEASES.md.; consultado em 2026-10-03.
