---
id: software.devops.tranche03.000205
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

# Requisitos de build em Linux e macOS e convenções de código para contribuidores

## Em uma frase
As seções Developing cert-manager, Contributing e Coding Conventions do README informam que o projeto suporta ambientes Linux e macOS para desenvolvimento — alertando especificamente que o macOS possui vários requisitos extras para garantir que ferramentas modernas estejam instaladas e disponíveis, documentados em cert-manager.io/docs/contributing/building/ — e que as diretrizes de estilo de código estão em cert-manager.io/docs/contributing/coding-conventions/.

## Por que importa
Contribuidores que tentam compilar e rodar a suíte de testes do cert-manager em macOS usando os utilitários BSD padrão do sistema sem instalar as ferramentas GNU/modernas exigidas pelo guia de build enfrentam falhas locais difíceis de diagnosticar.

## Como funciona
Antes de compilar o cert-manager a partir do código-fonte em macOS ou Linux, siga integralmente a página Building cert-manager e valide seu pull request contra as Coding Conventions oficiais.

## Exemplo
Um engenheiro usando macOS instala as dependências adicionais listadas em cert-manager.io/docs/contributing/building/ antes de executar os alvos de build e teste administrados pelo Prow CI.

## Limites e trade-offs
Sempre alinhe seu código às convenções documentadas em coding-conventions para evitar retrabalho durante a revisão dos mantenedores.

## Como verificar
Conferi as seções Developing cert-manager, Contributing e Coding Conventions no README oficial de cert-manager/cert-manager.

## Conexões
- [[certmanager-nginx-ingress-and-getting-started-guides]] — Veja também: Guias oficiais para emissão automática de TLS em Ingress (nginx-ingress) e primeiro certificado.
- [[certmanager-go-module-no-compatibility-guarantee]] — Veja também: Ausência de garantia de compatibilidade como módulo Go em pkg/ versus estabilidade de APIs Kubernetes.

## Fontes
- [cert-manager — GitHub README](https://raw.githubusercontent.com/cert-manager/cert-manager/master/README.md) — Visão geral do cert-manager para certificados e emissores no Kubernetes (ACME/Let's Encrypt, HashiCorp Vault, CyberArk, in-cluster), renovação automática, política de módulo Go e histórico kube-lego.; consultado em 2026-10-03.
- [cert-manager — Repositório Oficial no GitHub](https://github.com/cert-manager/cert-manager) — Repositório oficial do cert-manager na CNCF com código-fonte, SECURITY.md e notas de release.; consultado em 2026-10-03.
