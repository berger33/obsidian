---
id: software.devops.tranche13.001245
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

# Nydus: Verificação de Integridade Fim-a-Fim em Tempo de Execução (Árvore de Merkle com SHA-256 e BLAKE3)

## Em uma frase
Diferente das imagens OCI tradicionais — cujo digest SHA-256 é verificado apenas uma vez no momento do `pull` antes de extrair os arquivos para um diretório mutável —, o Nydus incorpora uma **árvore de Merkle** no `bootstrap` e valida criptograficamente (com **SHA-256** ou **BLAKE3**) tanto os metadados quanto cada chunk de dados lido em tempo de execução.

## Por que importa
Em um sistema de lazy pulling onde chunks de dados são buscados da rede ou de um cache compartilhado horas depois de o container ter iniciado, um chunk adulterado em trânsito ou no disco local poderia injetar código malicioso em execução se não houvesse validação por leitura.

## Como funciona
No RAFS, os nós internos da árvore no `bootstrap` contêm os hashes dos nós filhos e cada `OndiskChunkInfo` armazena o digest do chunk de 1 MB correspondente. Quando um processo dentro do container lê um bloco de arquivo, o Nydus verifica a sanidade dos campos do metadado e compara o hash calculado (SHA-256 ou BLAKE3) com o digest assinado na árvore; se houver qualquer divergência, a leitura é bloqueada imediatamente com erro `EINVAL`.

## Exemplo
```bash
# Verificar a integridade completa do bootstrap e dos blobs de uma imagem Nydus:
nydus-image check --bootstrap /var/lib/nydus/bootstrap --blobs-dir /var/lib/nydus/blobs
```

## Limites e trade-offs
Assumir que um erro de I/O (`EINVAL`) em um container Nydus é um bug da aplicação sem checar os logs do `nydusd` pode esconder uma falha de integridade de blob no backend de armazenamento.

## Como verificar
Monitore as métricas de erro de verificação de digest do `nydusd` via `nydusctl` e mantenha `BLAKE3` (mais rápido que SHA-256) habilitado na geração das imagens RAFS.

## Conexões
- [[nydus-ecossistema-ferramentas-nydusd-nydusify-nydus-image-nydusctl]] — Veja também: Nydus: Ferramentas do Ecossistema (nydusd, nydus-image, nydusify e nydusctl).
- [[nydus-prefetch-otimizacao-layout-io-amplification-cold-start]] — Veja também: Nydus: Tabela de Prefetch (PrefetchTable), Amplificação de I/O e Otimização de Leituras no Boot.

## Fontes
- [Nydus Image Service GitHub — README.md (RAFS On-Demand Layer Format, nydusify, nydusd, EROFS/FUSE & Containerd Snapshotter)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/docs/nydus-design.md) — README oficial do dragonflyoss/nydus detalhando o formato RAFS, inicialização de containers em milissegundos, ferramentas (nydus-image, nydusd, nydusify, nydusctl) e integração com Harbor e Dragonfly; consultado em 2026-10-03.
- [Nydus Official Architecture — docs/nydus-design.md (Bootstrap vs Data Blobs, Chunk Deduplication, Digest Authentication & Zran)](https://raw.githubusercontent.com/dragonflyoss/nydus/master/README.md) — Documento oficial de design arquitetural do Nydus explicando a separação entre metadados (bootstrap) e dados (blobs de chunks), verificação por Merkle tree e modos FUSE/virtiofs/EROFS; consultado em 2026-10-03.
- [Nydus Image Service — Official GitHub Repository](https://github.com/dragonflyoss/nydus) — Repositório oficial do Nydus no projeto Dragonfly; consultado em 2026-10-03.
