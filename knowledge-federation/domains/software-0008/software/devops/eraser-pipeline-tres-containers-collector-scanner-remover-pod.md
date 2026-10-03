---
id: software.devops.tranche15.001492
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://eraser-dev.github.io/eraser/docs/quick-start", "https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md", "https://github.com/eraser-dev/eraser"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Eraser: pipeline de três estágios por nó (`collector`, `scanner` e `remover`) nos Pods de limpeza

## Em uma frase
Por padrão, cada Pod de trabalho agendado pelo Eraser em um nó do cluster contém três containers sequenciais (`READY 0/3 Completed`): `collector`, `scanner` e `remover`.

## Por que importa
Separar a coleta do inventário CRI, o escaneamento de vulnerabilidades (como Trivy) e a exclusão de imagens em três containers distintos dentro do mesmo Pod permite isolar permissões, substituir o scanner ou desativá-lo completamente quando o objetivo é apenas limpar todas as imagens ociosas.

## Como funciona
O container `collector` conecta-se ao runtime do nó, lista todas as imagens em cache excluindo aquelas usadas por Pods ativos e envia a lista para o container `scanner`; o `scanner` verifica quais daquelas imagens ociosas possuem vulnerabilidades e repassa a lista de imagens não conformes ao container `remover`, que executa a remoção via API CRI.

## Exemplo
```bash
kubectl get pods -n eraser-system -o wide
kubectl describe pod -n eraser-system -l eraser.sh/type=collector
```

## Limites e trade-offs
Como os Pods por nó (`eraser-<node-name>-<hash>`) são jobs que rodam até a conclusão, ver `0/3 Completed` em `kubectl get pods -n eraser-system` é o estado normal de sucesso antes da coleta automática dos Pods finalizados.

## Como verificar
Inspecione os logs individuais de cada etapa com `kubectl logs -n eraser-system <eraser-pod> -c collector`, `-c scanner` e `-c remover`.

## Conexões
- [[eraser-arquitetura-limpeza-imagens-oci-nao-utilizadas-nos-kubernetes]] — Veja também: CNCF Eraser: arquitetura de limpeza automatizada de imagens não executadas e vulneráveis nos nós Kubernetes.
- [[eraser-agendamento-automatico-repeat-interval-configmap-scheduling]] — Veja também: Eraser: agendamento periódico de varredura (`manager.scheduling.repeatInterval`) via ConfigMap.

## Fontes
- [Eraser Official Documentation — Quick Start (DaemonSet Validation, Collector/Scanner/Remover Pipeline, repeatInterval & Scanner Toggle)](https://eraser-dev.github.io/eraser/docs/quick-start) — Guia oficial Quick Start do Eraser demonstrando a remoção automática de imagens não utilizadas e vulneráveis nos nós, configuração de repeatInterval e modo de 2 containers sem scanner; consultado em 2026-10-03.
- [Eraser GitHub — README.md (Cleaning Up Non-Running Images from Kubernetes Nodes & CNCF Governance)](https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md) — README oficial do eraser-dev/eraser (CNCF Sandbox) apresentando o escopo e a governança do projeto; consultado em 2026-10-03.
- [CNCF Eraser — Official GitHub Repository](https://github.com/eraser-dev/eraser) — Repositório oficial Apache-2.0 do Eraser; consultado em 2026-10-03.
