---
id: software.devops.tranche14.001387
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/containerd/nerdctl/main/README.md", "https://raw.githubusercontent.com/containerd/nerdctl/main/docs/command-reference.md", "https://github.com/containerd/nerdctl"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# nerdctl: Distribuição P2P Opcional de Imagens OCI sobre IPFS (ipfs://CID e nerdctl ipfs)

## Em uma frase
O `nerdctl` possui suporte opcional para distribuir e executar imagens de container diretamente sobre uma rede peer-to-peer **IPFS (InterPlanetary File System)** usando referências `ipfs://<CID>` e o comando `nerdctl ipfs registry serve`.

## Por que importa
Em laboratórios distribuídos ou redes locais onde múltiplos nós baixam imagens pesadas sem um servidor de registry centralizado dedicado, o IPFS permite compartilhar blocos endereçáveis por conteúdo entre os peers.

## Como funciona
Conforme destacado na documentação oficial, a integração IPFS é 100% opt-in (a máquina **nunca** é conectada a nenhuma rede P2P a menos que o usuário instale e inicie explicitamente o daemon `ipfs`); quando ativo, `nerdctl push ipfs://alpine:latest` publica a imagem no IPFS e retorna seu CID imutável para execução com `nerdctl run ipfs://<CID>`.

## Exemplo
```bash
# Exemplo opt-in quando um daemon IPFS local foi explicitamente iniciado:
nerdctl push ipfs://alpine:latest
```

## Limites e trade-offs
Publicar uma imagem contendo segredos internos em um daemon IPFS conectado à DHT pública da internet expõe os blocos da imagem globalmente para qualquer nó IPFS que conheça o CID.

## Como verificar
Para uso corporativo, configure o daemon IPFS em modo de rede privada isolada (`swarm.key`) antes de usar `nerdctl push ipfs://`.

## Conexões
- [[nerdctl-cosign-assinatura-verificacao-ocicrypt-imagens-criptografadas]] — Veja também: nerdctl: Assinatura e Verificação Cosign (--sign/--verify) e Criptografia de Camadas (ocicrypt).
- [[nerdctl-multi-platform-pull-save-load-oci-archives-inspect-native]] — Veja também: nerdctl: Operações Multi-Plataforma (--all-platforms), Arquivos Híbridos OCI/Docker e Inspeção Nativa.

## Fontes
- [nerdctl GitHub — README.md (Docker-Compatible CLI for containerd, Kubernetes Debugging in k8s.io, Rootless bypass4netns, Lazy-Pulling, ocicrypt, IPFS & Cosign)](https://raw.githubusercontent.com/containerd/nerdctl/main/README.md) — README oficial do containerd/nerdctl detalhando o uso com BuildKit/CNI, depuração de Kubernetes no namespace k8s.io, snapshotters (stargz, nydus, overlaybd, soci) e diferenciais frente ao Docker; consultado em 2026-10-03.
- [nerdctl Official Documentation — docs/command-reference.md (Container, Image, Compose, Namespace, AppArmor & IPFS Commands)](https://raw.githubusercontent.com/containerd/nerdctl/main/docs/command-reference.md) — Referência oficial completa de comandos e flags do nerdctl e nerdctl compose; consultado em 2026-10-03.
- [containerd nerdctl — Official GitHub Repository](https://github.com/containerd/nerdctl) — Repositório oficial Apache-2.0 do nerdctl; consultado em 2026-10-03.
