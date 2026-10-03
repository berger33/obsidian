---
id: software.devops.tranche13.001248
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md", "https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md", "https://github.com/dragonflyoss/nydus"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nydus: Implantação no Kubernetes e containerd com nydus-snapshotter e nerdctl

## Em uma frase
Para executar imagens Nydus em nós Kubernetes ou estações de trabalho com `nerdctl`, instala-se o plugin de snapshotter remoto **`containerd/nydus-snapshotter`** e configura-se o `containerd` (`config.toml`) para delegar a montagem de camadas Nydus ao `nydusd`.

## Por que importa
O snapshotter padrão `overlayfs` do `containerd` não compreende os media types de `bootstrap` e `blob` do RAFS e tentará baixar e extrair as camadas da forma tradicional se o proxy snapshotter não estiver registrado.

## Como funciona
No `/etc/containerd/config.toml`, registra-se o `[proxy_plugins.nydus]` apontando para o socket Unix `/run/containerd-nydus/containerd-nydus-grpc.sock` e define-se `snapshotter = "nydus"` e `disable_snapshot_annotations = false` na seção CRI. O `nydus-snapshotter` pode ser implantado em todos os nós do cluster Kubernetes como um `DaemonSet`.

## Exemplo
```toml
# Trecho em /etc/containerd/config.toml para ativar o nydus-snapshotter:
[proxy_plugins]
  [proxy_plugins.nydus]
    type = "snapshot"
    address = "/run/containerd-nydus/containerd-nydus-grpc.sock"

[plugins."io.containerd.grpc.v1.cri".containerd]
  snapshotter = "nydus"
  disable_snapshot_annotations = false
```

## Limites e trade-offs
Esquecer de configurar `disable_snapshot_annotations = false` no `/etc/containerd/config.toml` impede o `containerd` de repassar as anotações dos descritores de camada OCI para o `nydus-snapshotter`, fazendo o lazy pulling falhar.

## Como verificar
Verifique sempre que `disable_snapshot_annotations = false` está ativo no `containerd` e confirme o registro do plugin com `ctr plugins ls | grep nydus`.

## Conexões
- [[nydus-compatibilidade-oci-zran-estargz-conversao-harbor]] — Veja também: Nydus: Compatibilidade com Imagens OCI Nativas (OCI zran), eStargz e Conversão Automática no Harbor.
- [[nydus-kata-containers-virtiofs-confidential-containers-isolamento]] — Veja também: Nydus: Aceleração de Kata Containers (virtiofs) e Confidential Containers com Nydus.

## Fontes
- [Nydus Image Service GitHub — README.md (RAFS On-Demand Layer Format, nydusify, nydusd, EROFS/FUSE & Containerd Snapshotter)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md) — README oficial do dragonflyoss/nydus detalhando o formato RAFS, inicialização de containers em milissegundos, ferramentas (nydus-image, nydusd, nydusify, nydusctl) e integração com Harbor e Dragonfly; consultado em 2026-10-03.
- [Nydus Official Architecture — docs/nydus-design.md (Bootstrap vs Data Blobs, Chunk Deduplication, Digest Authentication & Zran)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md) — Documento oficial de design arquitetural do Nydus explicando a separação entre metadados (bootstrap) e dados (blobs de chunks), verificação por Merkle tree e modos FUSE/virtiofs/EROFS; consultado em 2026-10-03.
- [Nydus Image Service — Official GitHub Repository](https://github.com/dragonflyoss/nydus) — Repositório oficial do Nydus no projeto Dragonfly; consultado em 2026-10-03.
