---
id: software.devops.tranche03.000207
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
fontes: ["https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md", "https://github.com/cert-manager/cert-manager"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Transição do caminho de importação Go na versão 1.8: jetstack para cert-manager

## Em uma frase
Na seção Importing cert-manager as a Module, o README documenta que o caminho de importação Go (import path) para o cert-manager nas versões 1.8 e posteriores é github.com/cert-manager/cert-manager, enquanto para todas as versões anteriores à 1.8 (incluindo lançamentos menores e de patch daquelas séries) o caminho de importação é github.com/jetstack/cert-manager.

## Por que importa
Projetos legados em Go ou plugins externos de emissores (external issuers) escritos originalmente contra versões pré-1.8 falharão ao atualizar dependências se mantiverem o namespace antigo github.com/jetstack/cert-manager.

## Como funciona
Em qualquer projeto Go compatível com cert-manager 1.8+, utilize exclusivamente o caminho de módulo github.com/cert-manager/cert-manager no arquivo go.mod e nas declarações de import.

## Exemplo
Ao atualizar um webhook de DNS customizado de uma versão antiga para o cert-manager atual, o desenvolvedor substitui todas as importações de github.com/jetstack/cert-manager por github.com/cert-manager/cert-manager.

## Limites e trade-offs
Misturar ambos os caminhos de importação na mesma árvore de dependências Go causa conflitos de tipos duplicados e registro de esquemas do Kubernetes.

## Como verificar
Conferi os dois parágrafos finais da seção Importing cert-manager as a Module no README oficial de cert-manager/cert-manager.

## Conexões
- [[certmanager-go-module-no-compatibility-guarantee]] — Veja também: Ausência de garantia de compatibilidade como módulo Go em pkg/ versus estabilidade de APIs Kubernetes.
- [[certmanager-troubleshooting-and-slack-channels]] — Veja também: Fluxo de troubleshooting oficial e canais #cert-manager e #cert-manager-dev no Slack.

## Fontes
- [cert-manager — GitHub README](https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md) — Visão geral do cert-manager para certificados e emissores no Kubernetes (ACME/Let's Encrypt, HashiCorp Vault, CyberArk, in-cluster), renovação automática, política de módulo Go e histórico kube-lego.; consultado em 2026-10-03.
- [cert-manager — Repositório Oficial no GitHub](https://github.com/cert-manager/cert-manager) — Repositório oficial do cert-manager na CNCF com código-fonte, SECURITY.md e notas de release.; consultado em 2026-10-03.
