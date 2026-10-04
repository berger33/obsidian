---
id: software.seguranca.tranche08.000751
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/OJ/gobuster/master/README.md", "https://github.com/OJ/gobuster/wiki", "https://pkg.go.dev/github.com/OJ/gobuster/v3"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# **Gobuster (`OJ/gobuster`)**: Arquitetura de Enumeração Concorrente em Go (`dir`, `dns`, `vhost`, `s3`, `gcs`, `tftp` e `fuzz`) e Controle de Threads (`-t`)

## Em uma frase
**Gobuster** (`OJ/gobuster`, licença Apache-2.0, escrito em Go por OJ Reeves e Christian Mehlmauer) é uma ferramenta de linha de comando compilada de alta velocidade para descoberta por wordlist (*brute-force enumeration*) sem dependências de runtime (Java/Python).

## Por que importa
Conforme documentado no `README.md` oficial do repositório `OJ/gobuster`, a ferramenta organiza sua operação em sete modos especializados chamados por subcomando: **`gobuster dir`** (diretórios e arquivos web), **`gobuster dns`** (subdomínios DNS), **`gobuster vhost`** (*Virtual Hosts* HTTP por cabeçalho `Host`), **`gobuster s3`** (buckets públicos/privados AWS S3), **`gobuster gcs`** (buckets Google Cloud Storage), **`gobuster tftp`** (arquivos em servidores TFTP) e **`gobuster fuzz`** (fuzzing genérico com palavra-chave `FUZZ`).

## Como funciona
Cada modo compartilha o pool de *goroutines* concorrentes controlado globalmente por **`-t` / `--threads`** (padrão `10`), **`--delay`** (atraso entre requisições por thread, ex.: `150ms`) e **`-w` / `--wordlist`** (que aceita arquivo local ou **`-` para ler a wordlist diretamente de `stdin` via pipe**!).

## Exemplo
```bash
# Verificar a versao do Gobuster e listar todos os modos (subcomandos) e flags globais disponiveis
gobuster version
gobuster --help
```

## Limites e trade-offs
Ler a wordlist via **`-w -`** a partir de `stdin` permite gerar ou filtrar wordlists dinamicamente em memória (`hashcat --stdout ... | gobuster dir -u https://alvo -w -`) sem precisar gravar gigabytes de wordlists temporárias em disco.

## Como verificar
Execute `gobuster dir --help` para inspecionar as opções específicas do modo de diretórios.

## Conexões
- [[gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length]] — Veja também: Gobuster Modo **`dir`**: Descoberta de Diretórios e Arquivos Ocultos, Extensões (`-x`), Filtros de Status (`-s` / `-b`) e **`--exclude-length`**.
- [[gobuster-enumeracao-subdominios-dns-resolvers-wildcard-cname-ip]] — Referência cruzada direta com gobuster-enumeracao-subdominios-dns-resolvers-wildcard-cname-ip.

## Fontes
- [Gobuster Official GitHub — Modes (dir, vhost, dns, fuzz, s3, gcs, tftp) & CLI Reference](https://raw.githubusercontent.com/OJ/gobuster/master/README.md) — documentação oficial do Gobuster cobrindo todos os sete subcomandos, filtros de tamanho/status, mTLS, patterns e concorrência em Go; consultado em 2026-10-03.
- [Gobuster Official Wiki — Advanced Usage & Examples](https://github.com/OJ/gobuster/wiki) — wiki oficial do projeto Gobuster com exemplos práticos por subcomando; consultado em 2026-10-03.
- [Go Package Documentation — github.com/OJ/gobuster/v3](https://pkg.go.dev/github.com/OJ/gobuster/v3) — referência técnica dos pacotes internos do Gobuster v3 em Go; consultado em 2026-10-03.
