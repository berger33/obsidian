---
id: software.devops.tranche15.001470
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
fontes: ["https://spegel.dev/docs/getting-started/", "https://raw.githubusercontent.com/spegel-org/spegel/main/README.md", "https://github.com/spegel-org/spegel"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Spegel: considerações de segurança no compartilhamento de camadas entre nós e registries privados

## Em uma frase
Como o Spegel permite que qualquer nó do cluster solicite blobs de imagens presentes no `containerd` de outros nós do mesmo cluster, sua topologia pressupõe um modelo de confiança compartilhado entre os nós daquele cluster.

## Por que importa
Em clusters multi-tenant onde um tenant possui `imagePullSecrets` para baixar uma imagem privada no nó A, se o Spegel servir essa mesma imagem pelo digest/tag para o nó B sem reautenticar o segundo Pod no registry de origem, um Pod não autorizado poderia acessar a imagem já cacheada.

## Como funciona
Por essa razão, em ambientes multi-tenant estritos deve-se configurar quais registries são espelhados pelo Spegel (por exemplo restringindo a registries públicos ou internos compartilhados) ou habilitar políticas do Kubernetes como `AlwaysPullImages` admission controller quando exigido.

## Exemplo
```bash
kubectl get pods -n spegel -o jsonpath='{.items[0].spec.containers[0].args}'
```

## Limites e trade-offs
Sempre avalie os argumentos do container do Spegel (como filtros de registries espelhados) antes de usá-lo em clusters onde diferentes equipes não devem compartilhar imagens privadas entre si.

## Como verificar
Inspecione os argumentos (`args`) configurados no DaemonSet `spegel` para auditar a lista de registries habilitados para espelhamento.

## Conexões
- [[spegel-edge-computing-homelab-comparacao-dragonfly-harbor]] — Veja também: Spegel: aplicação em clusters Edge, homelabs e comparação arquitetural com Dragonfly e Harbor.

## Fontes
- [Spegel Official Documentation — Getting Started (Helm & Flux Deployment, Containerd Compatibility Matrix, EKS AL2023/Bottlerocket & /debug/web Verification)](https://spegel.dev/docs/getting-started/) — Guia oficial Getting Started do Spegel detalhando requisitos de containerd (config_path e discard_unpacked_layers = false), matriz de distribuições Kubernetes e validação via /debug/web; consultado em 2026-10-03.
- [Spegel GitHub — README.md (Stateless Cluster-Local OCI Registry Mirror Architecture & Features)](https://raw.githubusercontent.com/spegel-org/spegel/main/README.md) — README oficial do spegel-org/spegel explicando o cache P2P local de imagens, mitigação de rate-limiting e resiliência a quedas de registries externos; consultado em 2026-10-03.
- [Spegel — Official GitHub Repository](https://github.com/spegel-org/spegel) — Repositório oficial do Spegel; consultado em 2026-10-03.
