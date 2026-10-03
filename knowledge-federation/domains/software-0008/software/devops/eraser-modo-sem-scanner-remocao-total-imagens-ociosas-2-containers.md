---
id: software.devops.tranche15.001494
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

# Eraser: desativação do container `scanner` (`components.scanner.enabled: false`) para remoção total de imagens ociosas

## Em uma frase
Quando o administrador define `components.scanner.enabled: false` no ConfigMap do Eraser, os Pods por nó passam a rodar apenas 2 containers (`collector` e `remover`, exibindo `0/2 Completed`) e removem todas as imagens que não estão em execução no nó, independentemente de terem CVEs.

## Por que importa
Em clusters com discos pequenos nos worker nodes ou onde a política de segurança exige que absolutamente nenhuma imagem inativa permaneça armazenada em disco após o término dos Pods, pular a etapa de scan economiza CPU, memória e tempo de execução.

## Como funciona
Sem o container `scanner` no meio do pipeline, o `collector` identifica todas as imagens *non-running* no runtime CRI do nó e entrega a lista diretamente para o `remover`, que apaga todas elas (exceto imagens explicitamente protegidas em listas de exclusão).

## Exemplo
```yaml
components:
  scanner:
    enabled: false
```

## Limites e trade-offs
Ao desabilitar o `scanner` (`enabled: false`), imagens base grandes que são usadas apenas por CronJobs esporádicos (e que portanto não estão rodando no momento da limpeza) serão removidas do nó e precisarão ser baixadas novamente na próxima execução do CronJob.

## Como verificar
Execute `kubectl get pods -n eraser-system` durante o ciclo de limpeza e confirme que a coluna `READY` dos Pods de nó exibe `0/2` com status `Completed`.

## Conexões
- [[eraser-agendamento-automatico-repeat-interval-configmap-scheduling]] — Veja também: Eraser: agendamento periódico de varredura (`manager.scheduling.repeatInterval`) via ConfigMap.
- [[eraser-crd-imagelist-remocao-seletiva-lista-imagens-comprometidas]] — Veja também: Eraser: remoção sob demanda de imagens específicas em todo o cluster via CRD `ImageList`.

## Fontes
- [Eraser Official Documentation — Quick Start (DaemonSet Validation, Collector/Scanner/Remover Pipeline, repeatInterval & Scanner Toggle)](https://eraser-dev.github.io/eraser/docs/quick-start) — Guia oficial Quick Start do Eraser demonstrando a remoção automática de imagens não utilizadas e vulneráveis nos nós, configuração de repeatInterval e modo de 2 containers sem scanner; consultado em 2026-10-03.
- [Eraser GitHub — README.md (Cleaning Up Non-Running Images from Kubernetes Nodes & CNCF Governance)](https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md) — README oficial do eraser-dev/eraser (CNCF Sandbox) apresentando o escopo e a governança do projeto; consultado em 2026-10-03.
- [CNCF Eraser — Official GitHub Repository](https://github.com/eraser-dev/eraser) — Repositório oficial Apache-2.0 do Eraser; consultado em 2026-10-03.
