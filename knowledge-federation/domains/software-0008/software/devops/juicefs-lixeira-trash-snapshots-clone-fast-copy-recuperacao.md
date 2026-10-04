---
id: software.devops.tranche18.001720
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-18.md"
fontes: ["https://juicefs.com/docs/community/architecture/", "https://raw.githubusercontent.com/juicedata/juicefs/main/README.md", "https://github.com/juicedata/juicefs"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# JuiceFS: proteção contra exclusão acidental com Lixeira (`--trash-days`) e clonagem instantânea de metadados

## Em uma frase
O JuiceFS inclui uma lixeira interna configurável (`--trash-days`, padrão de 1 dia) que retém arquivos deletados em um diretório oculto `.trash` antes de apagar fisicamente seus blocos no Object Storage, além de permitir clonagem rápida de diretórios inteiros apenas copiando referências de metadados.

## Por que importa
Um `rm -rf` acidental em um diretório de 50 TB compartilhado entre dezenas de Pods destruiria instantaneamente dados críticos se os blocos no S3 fossem deletados de forma síncrona na chamada `unlink`.

## Como funciona
Quando `unlink` é chamado e `--trash-days` é maior que `0`, o JuiceFS move apenas a entrada de metadados para `.trash/YYYY-MM-DD-HH/` em tempo constante $O(1)$, permitindo restaurar arquivos com um simples `mv` de volta para o diretório original até o prazo de expiração.

## Exemplo
```bash
# Configurando retenção de lixeira de 7 dias no volume JuiceFS:
juicefs config redis://:password@redis-meta.internal:6379/1 --trash-days 7
ls -la /mnt/jfs/.trash/
```

## Limites e trade-offs
Arquivos retidos dentro de `.trash` continuam contabilizados no consumo de capacidade do Object Storage até que expirem ou sejam esvaziados explicitamente.

## Como verificar
Teste a remoção de um arquivo de teste em `/mnt/jfs/`, localize-o dentro de `/mnt/jfs/.trash/` e restaure-o com `mv` para validar o procedimento de recuperação.

## Conexões
- [[juicefs-locks-globais-posix-fcntl-flock-consistencia-multi-cliente]] — Veja também: JuiceFS: locks distribuídos de arquivos (`flock` BSD e `fcntl` POSIX) e semântica de consistência.

## Fontes
- [JuiceFS GitHub — README.md (High-Performance POSIX Cloud-Native File System, Object Storage + Metadata Engine Architecture)](https://juicefs.com/docs/community/architecture/) — README oficial do juicedata/juicefs apresentando compatibilidade POSIX/Hadoop/S3, consistência forte, locks globais, criptografia e compressão; consultado em 2026-10-03.
- [JuiceFS Official Documentation — Architecture (JuiceFS Client, Data Storage, Metadata Engine & Chunks/Slices/Blocks Layout)](https://raw.githubusercontent.com/juicedata/juicefs/main/README.md) — Documentação oficial de arquitetura do JuiceFS detalhando Chunks de 64 MiB, Slices append-only, Blocks de 4 MiB, compactação e métodos de acesso; consultado em 2026-10-03.
- [JuiceFS — Official GitHub Repository](https://github.com/juicedata/juicefs) — Repositório oficial Apache-2.0 do JuiceFS; consultado em 2026-10-03.
