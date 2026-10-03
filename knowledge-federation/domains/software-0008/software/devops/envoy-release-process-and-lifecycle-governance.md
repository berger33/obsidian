---
id: software.devops.tranche03.000280
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

# Processo formal de lançamento e governança de versões em RELEASES.md

## Em uma frase
A seção final `Releases` do README aponta para o documento oficial `RELEASES.md` (`github.com/envoyproxy/envoy/blob/main/RELEASES.md`), complementado pelos selos de conformidade OpenSSF Best Practices (`projects/1266`), OpenSSF Scorecard e CLOMonitor da CNCF no topo do documento.

## Por que importa
Como o Envoy recebe correções frequentes de segurança para protocolos HTTP/1.1, HTTP/2, HTTP/3 (QUIC) e gRPC, conhecer o ciclo de vida e as janelas de suporte documentadas em `RELEASES.md` é indispensável para manter proxies de borda e malhas de serviços em versões suportadas.

## Como funciona
Consulte `RELEASES.md` para alinhar o calendário de upgrades dos seus proxies Envoy (ou dos controladores que o embutem) às versões estáveis ativamente mantidas.

## Exemplo
A equipe de plataforma agenda janelas regulares de atualização das imagens do Envoy seguindo a política de ciclo de vida descrita em `RELEASES.md`.

## Limites e trade-offs
Deixar instâncias de Envoy expostas à internet em versões que já saíram da janela de manutenção de `RELEASES.md` deixa a borda vulnerável a CVEs públicas de HTTP/2 e TLS.

## Como verificar
Conferi os badges de topo e a seção Releases no README oficial de envoyproxy/envoy.

## Conexões
- [[envoy-oss-fuzzing-and-ppc64le-security-policy-exclusion]] — Veja também: Integração contínua com OSS-Fuzz e exclusão da arquitetura ppc64le da política de segurança.

## Fontes
- [Envoy Proxy — GitHub README](https://raw.githubusercontent.com/envoyproxy/envoy/main/README.md) — Visão geral do Envoy (edge/middle/service proxy na CNCF, artigos de arquitetura sobre threading, hot restart, stats e xDS, repositórios relacionados, listas de e-mail, reuniões, auditorias Cure53/Ada Logics, OSS-Fuzz e política ppc64le).; consultado em 2026-10-03.
- [Envoy Proxy — Repositório Oficial no GitHub](https://github.com/envoyproxy/envoy) — Repositório oficial do Envoy Proxy com código-fonte C++, api/, docs/security/, DEVELOPER.md, SECURITY.md e RELEASES.md.; consultado em 2026-10-03.
