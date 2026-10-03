---
id: software.devops.tranche02.000136
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-02.md"
fontes: ["https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md", "https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Fluxo de instalação em duas etapas (--crds e control plane), linkerd check e linkerd inject

## Em uma frase
A seção `Comprehensive` de `BUILD.md` documenta a sequência recomendada de instalação e verificação do Linkerd em um cluster Kubernetes: aplicar primeiro as CRDs (`linkerd install --crds | kubectl apply -f -`), aplicar em seguida o plano de controle (`linkerd install | kubectl apply -f -`), instalar a extensão de visualização (`linkerd viz install | kubectl apply -f -`), validar versões e saúde com `linkerd version` e `linkerd check`, e injetar aplicações com `linkerd inject - | kubectl apply -f -`.

## Por que importa
Separar a instalação das CRDs da instalação dos controladores evita condições de corrida no API Server do Kubernetes, enquanto o comando `linkerd check` executa validações pré e pós-instalação que detectam permissões ou configurações ausentes imediatamente.

## Como funciona
Em pipelines declarativos ou implantações manuais, aplique sempre `linkerd install --crds` antes do control plane e incorpore `linkerd check` como gate obrigatório de verificação após qualquer instalação ou upgrade.

## Exemplo
Durante o provisionamento de um cluster local `k3d`, o engenheiro instala CRDs e control plane do Linkerd, valida tudo com `linkerd check` e injeta a aplicação de demonstração `emojivoto`.

## Limites e trade-offs
Executar `linkerd install` antes de registrar as CRDs com `linkerd install --crds` fará o `kubectl apply` falhar por tipos de recursos desconhecidos.

## Como verificar
Conferi a seção Comprehensive em `BUILD.md` de `linkerd/linkerd2`.

## Conexões
- [[linkerd-multicluster-gateway-and-service-mirror]] — Veja também: Extensão multicluster: linkerd-gateway e controlador linkerd-service-mirror.
- [[linkerd-control-plane-distributed-tracing-flag]] — Veja também: Habilitação de rastreamento distribuído nos componentes do control plane.

## Fontes
- [Linkerd2 — Development and Architecture Guide (BUILD.md)](https://raw.githubusercontent.com/linkerd/linkerd2/main/BUILD.md) — Guia oficial de arquitetura e build do Linkerd2 detalhando control plane em Go/React (destination, proxy-injector, identity), extensões viz e multicluster, data plane em Rust e flags de tracing.; consultado em 2026-10-03.
- [Linkerd2 — GitHub README](https://raw.githubusercontent.com/linkerd/linkerd2/main/README.md) — Visão geral do Linkerd como service mesh ultraleve e security-first na CNCF, layout dos 5 repositórios, auditorias de segurança em audits/, Steering Committee e licença Apache 2.0.; consultado em 2026-10-03.
