---
id: software.devops.tranche03.000206
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
fontes: ["https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md", "https://cert-manager.io/docs/getting-started/"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Ausência de garantia de compatibilidade como módulo Go em pkg/ versus estabilidade de APIs Kubernetes

## Em uma frase
A seção Importing cert-manager as a Module do README traz um aviso explícito com símbolo de alerta: o cert-manager não oferece atualmente garantia de compatibilidade de módulo Go (Go module compatibility guarantee), o que significa que a maior parte do código sob pkg/ está sujeita a mudanças incompatíveis (breaking changes) mesmo entre releases menores ou de patch e mesmo que os símbolos sejam exportados publicamente; em contrapartida, isso não afeta as garantias de versão de API sob a Kubernetes Deprecation Policy.

## Por que importa
Equipes que constroem operadores ou integrações em Go importando pacotes internos de pkg/ do cert-manager precisam saber que uma simples atualização de patch pode quebrar a compilação Go, enquanto os tipos de API Kubernetes (CRDs) seguem a política formal de depreciação do Kubernetes.

## Como funciona
Ao integrar sistemas em Go com o cert-manager, restrinja o acoplamento aos tipos da API declarativa do Kubernetes e consulte o guia oficial Importing cert-manager in Go (cert-manager.io/docs/contributing/importing/) antes de atualizar a dependência no go.mod.

## Exemplo
Um operador interno que gera recursos Certificate importa a definição da API do cert-manager e fixa a versão exata no go.mod, testando qualquer atualização de patch em CI.

## Limites e trade-offs
Nunca presuma SemVer estrito para funções internas dentro de pkg/ do repositório cert-manager/cert-manager.

## Como verificar
Conferi a seção Importing cert-manager as a Module no README oficial de cert-manager/cert-manager.

## Conexões
- [[certmanager-linux-macos-development-and-coding-conventions]] — Veja também: Requisitos de build em Linux e macOS e convenções de código para contribuidores.
- [[certmanager-go-import-path-v1-8-transition]] — Veja também: Transição do caminho de importação Go na versão 1.8: jetstack para cert-manager.

## Fontes
- [cert-manager — GitHub README](https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md) — Visão geral do cert-manager para certificados e emissores no Kubernetes (ACME/Let's Encrypt, HashiCorp Vault, CyberArk, in-cluster), renovação automática, política de módulo Go e histórico kube-lego.; consultado em 2026-10-03.
- [cert-manager Documentation — Getting Started & Installation](https://cert-manager.io/docs/getting-started/) — Documentação oficial do cert-manager cobrindo instalação, configuração de Issuers/Certificates, nginx-ingress e troubleshooting.; consultado em 2026-10-03.
