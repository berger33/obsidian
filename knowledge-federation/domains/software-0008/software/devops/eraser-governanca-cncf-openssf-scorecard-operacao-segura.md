---
id: software.devops.tranche15.001500
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
fontes: ["https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md", "https://eraser-dev.github.io/eraser/docs/quick-start", "https://github.com/eraser-dev/eraser"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Eraser: governança CNCF, OpenSSF Scorecard e boas práticas operacionais com registries e mirrors

## Em uma frase
Mantido na CNCF com verificação contínua de OpenSSF Best Practices, OpenSSF Scorecard e FOSSA, o Eraser integra-se à pilha de segurança e gerenciamento de imagens ao lado de ferramentas como Trivy, Copacetic e Spegel.

## Por que importa
Em um cluster bem governado, o ciclo completo de higiene de imagens combina patching rápido de imagens ativas (Copacetic), espelhamento P2P de imagens em uso (Spegel) e expurgo automático de imagens inativas e vulneráveis do cache dos nós (Eraser).

## Como funciona
Como os Pods do Eraser precisam conversar diretamente com o socket CRI do nó (`/run/containerd/containerd.sock` ou equivalente) para listar e deletar imagens, eles rodam isolados no namespace administrativo `eraser-system` sob controle estrito de RBAC e Pod Security.

## Exemplo
```bash
kubectl get all -n eraser-system
```

## Limites e trade-offs
Se o cluster utilizar o Spegel para espelhar camadas P2P entre nós, lembre-se de que quando o Eraser remove uma imagem não executada de todos os nós do cluster, o próximo Pod que solicitar aquela imagem fará pull novamente do registry upstream.

## Como verificar
Audite os recursos e permissões em `eraser-system` com `kubectl get deploy,cm,sa -n eraser-system` para validar a conformidade da instalação.

## Conexões
- [[eraser-crd-imagejob-execucao-efemera-node-selectors-limpeza]] — Veja também: Eraser: coordenação distribuída de pods de limpeza por nó via recurso `ImageJob`.

## Fontes
- [Eraser Official Documentation — Quick Start (DaemonSet Validation, Collector/Scanner/Remover Pipeline, repeatInterval & Scanner Toggle)](https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md) — Guia oficial Quick Start do Eraser demonstrando a remoção automática de imagens não utilizadas e vulneráveis nos nós, configuração de repeatInterval e modo de 2 containers sem scanner; consultado em 2026-10-03.
- [Eraser GitHub — README.md (Cleaning Up Non-Running Images from Kubernetes Nodes & CNCF Governance)](https://eraser-dev.github.io/eraser/docs/quick-start) — README oficial do eraser-dev/eraser (CNCF Sandbox) apresentando o escopo e a governança do projeto; consultado em 2026-10-03.
- [CNCF Eraser — Official GitHub Repository](https://github.com/eraser-dev/eraser) — Repositório oficial Apache-2.0 do Eraser; consultado em 2026-10-03.
