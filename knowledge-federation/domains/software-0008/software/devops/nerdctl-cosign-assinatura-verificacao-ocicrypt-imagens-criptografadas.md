---
id: software.devops.tranche14.001386
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

# nerdctl: Assinatura e Verificação Cosign (--sign/--verify) e Criptografia de Camadas (ocicrypt)

## Em uma frase
O `nerdctl` integra nativamente segurança de supply chain e confidencialidade de imagens através de duas funcionalidades avançadas: assinatura/verificação com **Sigstore Cosign** (`nerdctl push --sign=cosign` e `nerdctl pull/run --verify=cosign`) e criptografia de camadas OCI com **ocicrypt** (`nerdctl image encrypt` e `nerdctl image decrypt`).

## Por que importa
Quando uma imagem contém modelos proprietários de IA ou algoritmos confidenciais que precisam ser armazenados em um registry compartilhado, assinar a imagem garante integridade, mas somente criptografar as camadas (`ocicrypt`) impede a leitura não autorizada do conteúdo.

## Como funciona
Com `nerdctl image encrypt --recipient=jwe:mypubkey.pem src:v1 dst:v1-enc`, as camadas da imagem são criptografadas com a chave pública do destinatário e só podem ser descriptografadas nos nós que possuem a chave privada correspondente; já `--verify=cosign --cosign-key cosign.pub` bloqueia o pull/execução de qualquer imagem sem assinatura válida.

## Exemplo
```bash
nerdctl push --sign=cosign --cosign-key cosign.key ghcr.io/org/app:v1.0.0
nerdctl run --rm --verify=cosign --cosign-key cosign.pub ghcr.io/org/app:v1.0.0
```

## Limites e trade-offs
Executar `nerdctl push --sign=cosign` sem ter o binário `cosign` instalado no `PATH` da máquina falha porque o `nerdctl` invoca a CLI do Cosign para processar as assinaturas.

## Como verificar
Certifique-se de que o binário `cosign` esteja instalado no `PATH` ao usar `--sign=cosign` ou `--verify=cosign` no `nerdctl`.

## Conexões
- [[nerdctl-compose-up-down-execucao-docker-compose-containerd]] — Veja também: nerdctl: Orquestração Multi-Container Compatível com Compose Spec (nerdctl compose).
- [[nerdctl-ipfs-p2p-image-distribution-offline-optional]] — Veja também: nerdctl: Distribuição P2P Opcional de Imagens OCI sobre IPFS (ipfs://CID e nerdctl ipfs).

## Fontes
- [nerdctl GitHub — README.md (Docker-Compatible CLI for containerd, Kubernetes Debugging in k8s.io, Rootless bypass4netns, Lazy-Pulling, ocicrypt, IPFS & Cosign)](https://raw.githubusercontent.com/containerd/nerdctl/main/README.md) — README oficial do containerd/nerdctl detalhando o uso com BuildKit/CNI, depuração de Kubernetes no namespace k8s.io, snapshotters (stargz, nydus, overlaybd, soci) e diferenciais frente ao Docker; consultado em 2026-10-03.
- [nerdctl Official Documentation — docs/command-reference.md (Container, Image, Compose, Namespace, AppArmor & IPFS Commands)](https://raw.githubusercontent.com/containerd/nerdctl/main/docs/command-reference.md) — Referência oficial completa de comandos e flags do nerdctl e nerdctl compose; consultado em 2026-10-03.
- [containerd nerdctl — Official GitHub Repository](https://github.com/containerd/nerdctl) — Repositório oficial Apache-2.0 do nerdctl; consultado em 2026-10-03.
