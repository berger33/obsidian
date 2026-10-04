---
id: software.devops.tranche13.001246
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
fontes: ["https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md", "https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md", "https://github.com/dragonflyoss/nydus"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Nydus: Tabela de Prefetch (PrefetchTable), Amplificação de I/O e Otimização de Leituras no Boot

## Em uma frase
Para mitigar a latência de buscar chunks remotos individualmente logo após o container iniciar, o Nydus suporta uma **PrefetchTable** (`s_prefetch_table_offset` no superbloco RAFS) e amplificação controlada de I/O de usuário (`User I/O amplification`) que pré-carregam em background os arquivos e diretórios necessários para o boot.

## Por que importa
Quando um runtime como Python, Node.js ou JVM inicializa, ele importa dezenas de arquivos `.py`, `.js` ou `.jar` nos primeiros 2 segundos; buscar cada arquivo em uma requisição HTTP separada de 1 MB geraria centenas de round-trips de rede.

## Como funciona
Durante a conversão da imagem com `nydusify`, o operador pode passar pela entrada padrão (`stdin` / `--prefetch-patterns`) a lista de caminhos de arquivos e diretórios críticos de inicialização. Esses inodes são gravados na `PrefetchTable` do `bootstrap`; assim que o container monta o filesystem, o `nydusd` dispara threads em background para baixar e popular esses chunks no `blobcache` local em leituras coalescidas maiores.

## Exemplo
```bash
# Converter imagem com lista explicita de caminhos para prefetch em background:
cat << 'EOF' | nydusify convert --source ghcr.io/org/api:v1 --target ghcr.io/org/api:v1-nydus --prefetch-patterns
/app/bin/server
/app/config/
/usr/lib/x86_64-linux-gnu/
EOF
```

## Limites e trade-offs
Colocar a raiz inteira `/` na lista de `--prefetch-patterns` faz o `nydusd` baixar imediatamente 100% da imagem em background em todos os nós, anulando a economia de banda e disco do lazy pulling.

## Como verificar
Inclua em `--prefetch-patterns` apenas os binários, bibliotecas compartilhadas e arquivos de configuração efetivamente abertos durante a inicialização da aplicação.

## Conexões
- [[nydus-integridade-fim-a-fim-merkle-tree-sha256-blake3]] — Veja também: Nydus: Verificação de Integridade Fim-a-Fim em Tempo de Execução (Árvore de Merkle com SHA-256 e BLAKE3).
- [[nydus-compatibilidade-oci-zran-estargz-conversao-harbor]] — Veja também: Nydus: Compatibilidade com Imagens OCI Nativas (OCI zran), eStargz e Conversão Automática no Harbor.

## Fontes
- [Nydus Image Service GitHub — README.md (RAFS On-Demand Layer Format, nydusify, nydusd, EROFS/FUSE & Containerd Snapshotter)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md) — README oficial do dragonflyoss/nydus detalhando o formato RAFS, inicialização de containers em milissegundos, ferramentas (nydus-image, nydusd, nydusify, nydusctl) e integração com Harbor e Dragonfly; consultado em 2026-10-03.
- [Nydus Official Architecture — docs/nydus-design.md (Bootstrap vs Data Blobs, Chunk Deduplication, Digest Authentication & Zran)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md) — Documento oficial de design arquitetural do Nydus explicando a separação entre metadados (bootstrap) e dados (blobs de chunks), verificação por Merkle tree e modos FUSE/virtiofs/EROFS; consultado em 2026-10-03.
- [Nydus Image Service — Official GitHub Repository](https://github.com/dragonflyoss/nydus) — Repositório oficial do Nydus no projeto Dragonfly; consultado em 2026-10-03.
