---
id: software.devops.tranche15.001495
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

# Eraser: remoção sob demanda de imagens específicas em todo o cluster via CRD `ImageList`

## Em uma frase
O Custom Resource `ImageList` (`eraser.sh`) permite que administradores especifiquem uma lista explícita de imagens (ou curingas `*` para limpar todas as não utilizadas) que devem ser banidas e removidas imediatamente do cache de todos os nós do cluster.

## Por que importa
Quando um alerta de segurança ou incidente de supply chain identifica que uma versão específica de imagem (como `alpine:3.7.3` ou uma tag interna revogada) possui vulnerabilidade crítica, o administrador pode expurgá-la de todos os nós sem esperar pelo próximo ciclo de 24 horas.

## Como funciona
Ao aplicar ou atualizar o objeto `ImageList` (por exemplo com nome `imagelist`), o `eraser-controller-manager` dispara imediatamente um `ImageJob` que percorre todos os nós do cluster e remove todas as imagens especificadas em `spec.images` que não estejam em execução.

## Exemplo
```yaml
apiVersion: eraser.sh/v1
kind: ImageList
metadata:
  name: imagelist
spec:
  images:
    - docker.io/library/alpine:3.7.3
    - ghcr.io/org/vulnerable-app:1.0.0
```

## Limites e trade-offs
Se uma imagem listada em `ImageList` ainda estiver sendo executada por um Pod ativo ou DaemonSet em algum nó, o Eraser não poderá removê-la daquele nó enquanto o Pod não for encerrado ou atualizado.

## Como verificar
Aplique o manifesto `ImageList`, aguarde os Pods em `eraser-system` completarem e valide no nó com `crictl images` que a imagem alvo foi removida.

## Conexões
- [[eraser-modo-sem-scanner-remocao-total-imagens-ociosas-2-containers]] — Veja também: Eraser: desativação do container `scanner` (`components.scanner.enabled: false`) para remoção total de imagens ociosas.
- [[eraser-exclusao-imagens-protegidas-excluded-configmap-pause-cache]] — Veja também: Eraser: listas de exclusão (`eraser.sh/cleanup.exclude`) para proteger imagens críticas e pré-cacheadas.

## Fontes
- [Eraser Official Documentation — Quick Start (DaemonSet Validation, Collector/Scanner/Remover Pipeline, repeatInterval & Scanner Toggle)](https://eraser-dev.github.io/eraser/docs/quick-start) — Guia oficial Quick Start do Eraser demonstrando a remoção automática de imagens não utilizadas e vulneráveis nos nós, configuração de repeatInterval e modo de 2 containers sem scanner; consultado em 2026-10-03.
- [Eraser GitHub — README.md (Cleaning Up Non-Running Images from Kubernetes Nodes & CNCF Governance)](https://raw.githubusercontent.com/eraser-dev/eraser/main/README.md) — README oficial do eraser-dev/eraser (CNCF Sandbox) apresentando o escopo e a governança do projeto; consultado em 2026-10-03.
- [CNCF Eraser — Official GitHub Repository](https://github.com/eraser-dev/eraser) — Repositório oficial Apache-2.0 do Eraser; consultado em 2026-10-03.
