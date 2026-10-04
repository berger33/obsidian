---
id: software.devops.tranche13.001235
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
fontes: ["https://raw.githubusercontent.com/dragonflyoss/dragonfly/main/README.md", "https://d7y.io/docs/next/", "https://github.com/dragonflyoss/dragonfly"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Dragonfly: Aceleração P2P de Pesos de Modelos de IA/ML, Objetos S3/OSS e Datasets em Clusters GPU

## Em uma frase
Além de imagens de containers OCI, o Dragonfly é amplamente utilizado em infraestruturas de IA/ML para distribuir via P2P pesos de modelos de linguagem (LLMs do Hugging Face, PyTorch checkpoints, safetensors) e grandes datasets armazenados em S3, GCS, Azure Blob ou OSS.

## Por que importa
Quando um job de treinamento distribuído ou uma frota de servidores de inferência vLLM/Triton escala para dezenas de nós GPU simultaneamente, baixar um modelo de 70 GB de um bucket S3 em cada nó leva dezenas de minutos e gera custos elevados de transferência.

## Como funciona
Por meio do proxy HTTP/HTTPS do Peer, de plugins de SDK (como integração com Hugging Face Hub / `dfget` CLI) ou armazenamento de objetos via `dfstore`, os downloads de arquivos `.safetensors` e `.bin` são fatiados em peças e distribuídos entre a memória/NVMe dos nós GPU pela rede local de alta velocidade.

## Exemplo
```bash
# Exemplo de download acelerado via P2P de um artefato pesado usando dfget:
dfget https://model-bucket.s3.amazonaws.com/llm-70b/model-00001-of-00015.safetensors \
  --output /models/model-00001.safetensors
```

## Limites e trade-offs
Armazenar o cache de peças do `dfdaemon` no disco raiz pequeno do sistema operacional ao baixar modelos de IA de centenas de gigabytes esgota o disco do nó (`DiskPressure`) e causa despejo (`Eviction`) de Pods.

## Como verificar
Monte um volume dedicado de alta capacidade (NVMe local) para o diretório de cache de dados do `Peer` e configure políticas de limpeza de cache por limite de uso de disco.

## Conexões
- [[dragonfly-integracao-containerd-cri-o-docker-mirror-proxy]] — Veja também: Dragonfly: Integração Não-Intrusiva com containerd, CRI-O e Docker para Pull de Imagens OCI.
- [[dragonfly-manager-console-multi-cluster-configuracao-dinamica]] — Veja também: Dragonfly: Componente Manager para Governança Multi-Cluster P2P e Configuração Dinâmica.

## Fontes
- [Dragonfly GitHub — README.md (P2P File & Image Distribution, Architecture: Manager, Scheduler, Seed Peer & Dfdaemon in Rust)](https://raw.githubusercontent.com/dragonflyoss/dragonfly/main/README.md) — README oficial do dragonflyoss/dragonfly (CNCF Incubating) descrevendo a arquitetura P2P, cliente Dfdaemon reescrito em Rust (v2.1.0+), isolamento de I/O, integração com Nydus e modelos de IA; consultado em 2026-10-03.
- [Dragonfly Official Documentation — d7y.io/docs/next/ (Quickstart, Containerd Mirror, Preheat & Observability)](https://d7y.io/docs/next/) — Documentação oficial do Dragonfly sobre configuração de mirror no containerd, dfget, dfcache, preheat de imagens/modelos e métricas; consultado em 2026-10-03.
- [Dragonfly — Official GitHub Repository](https://github.com/dragonflyoss/dragonfly) — Repositório oficial do Dragonfly na CNCF; consultado em 2026-10-03.
