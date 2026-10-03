---
id: software.devops.tranche15.001493
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

# Eraser: agendamento periódico de varredura (`manager.scheduling.repeatInterval`) via ConfigMap

## Em uma frase
Após ser implantado no cluster, o Eraser executa ciclos automáticos de limpeza em intervalos regulares governados pela chave `manager.scheduling.repeatInterval` na configuração do gerenciador.

## Por que importa
Permite manter a higiene contínua do cache de imagens dos nós (por exemplo a cada 24 horas ou a cada 6 horas em clusters de CI/CD com intenso churn de tags) sem necessidade de intervenção manual ou CronJobs externos.

## Como funciona
O intervalo padrão de repetição é de 24 horas (`24h`), aceitando unidades de tempo válidas em formato Go: `"ns"`, `"us"` (ou `"µs"`), `"ms"`, `"s"`, `"m"` e `"h"`. A cada ciclo, o `eraser-controller-manager` instancia os Pods nos nós, aguarda a conclusão de todos eles e agenda a próxima execução.

## Exemplo
```yaml
manager:
  scheduling:
    repeatInterval: "12h"
    beginImmediately: true
```

## Limites e trade-offs
Definir um `repeatInterval` excessivamente curto (como poucos minutos) com o container `scanner` habilitado em clusters grandes causará consumo desnecessário de CPU nos nós devido às varreduras repetidas de vulnerabilidades.

## Como verificar
Verifique o ConfigMap de configuração no namespace `eraser-system` (`kubectl get cm -n eraser-system -o yaml`) e acompanhe a criação periódica dos Pods nos logs do `eraser-controller-manager`.

## Conexões
- [[eraser-pipeline-tres-containers-collector-scanner-remover-pod]] — Veja também: Eraser: pipeline de três estágios por nó (`collector`, `scanner` e `remover`) nos Pods de limpeza.
- [[eraser-modo-sem-scanner-remocao-total-imagens-ociosas-2-containers]] — Veja também: Eraser: desativação do container `scanner` (`components.scanner.enabled: false`) para remoção total de imagens ociosas.

## Fontes
- [Eraser Official Documentation — Quick Start (DaemonSet Validation, Collector/Scanner/Remover Pipeline, repeatInterval & Scanner Toggle)](https://eraser-dev.github.io/eraser/docs/quick-start) — Guia oficial Quick Start do Eraser demonstrando a remoção automática de imagens não utilizadas e vulneráveis nos nós, configuração de repeatInterval e modo de 2 containers sem scanner; consultado em 2026-10-03.
- [Eraser GitHub — README.md (Cleaning Up Non-Running Images from Kubernetes Nodes & CNCF Governance)](https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md) — README oficial do eraser-dev/eraser (CNCF Sandbox) apresentando o escopo e a governança do projeto; consultado em 2026-10-03.
- [CNCF Eraser — Official GitHub Repository](https://github.com/eraser-dev/eraser) — Repositório oficial Apache-2.0 do Eraser; consultado em 2026-10-03.
