---
id: software.seguranca.tranche08.000752
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

# Gobuster Modo **`dir`**: Descoberta de Diretórios e Arquivos Ocultos, Extensões (`-x`), Filtros de Status (`-s` / `-b`) e **`--exclude-length`**

## Em uma frase
No modo clássico **`gobuster dir -u <URL> -w <wordlist>`**, o Gobuster testa caminhos web e pode anexar automaticamente múltiplas extensões de arquivo de backup ou código-fonte a cada palavra da lista usando **`-x`** (ex.: `-x php,bak,old,env,json,yml,sql,zip`) ou ler extensões de um arquivo com `-X`.

## Por que importa
Aplicações web modernas, proxies reversos e Single-Page Applications (SPAs) frequentemente respondem a qualquer URL inexistente com código `200 OK` (ou `403`/`302` customizado) exibindo uma página padrão de erro ("Soft 404") de tamanho fixo: se você não filtrar esse comportamento, o Gobuster abortará avisando que o servidor respondeu `200` para o teste de caminho aleatório.

## Como funciona
Para contornar respostas *Wildcard / Soft-404* com precisão cirúrgica, use **`-b` (`--status-codes-blacklist`)** para ignorar códigos indesejados e **`--exclude-length`** (que aceita tamanhos exatos e faixas, ex.: `--exclude-length 1420,1500-1550`) para descartar respostas que tenham exatamente a quantidade de bytes da página de erro padrão!

## Exemplo
```bash
# Enumerar diretorios e arquivos de configuracao/backup filtrando respostas Soft-404 de tamanho 1420 bytes
gobuster dir -u https://app.internal.corp \
  -w /usr/share/seclists/Discovery/Web-Content/raft-medium-words.txt \
  -x php,bak,old,json,yml,txt \
  -b 404,429 \
  --exclude-length 1420 \
  -t 20 --timeout 10s -o /cases/pentest/gobuster_dir.txt
```

## Limites e trade-offs
Adicione a flag **`-f` (`--add-slash`)** quando estiver enumerando servidores web ou proxies (como configurações específicas de Nginx/Spring/Django) que só respondem `200`/`301` para diretórios se a URL terminar explicitamente com barra `/`.

## Como verificar
Verifique na saída (`-o`) o código de status `(Status: 200)` e o tamanho `[Size: ...]` de cada caminho descoberto.

## Conexões
- [[gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz]] — Veja também: **Gobuster (`OJ/gobuster`)**: Arquitetura de Enumeração Concorrente em Go (`dir`, `dns`, `vhost`, `s3`, `gcs`, `tftp` e `fuzz`) e Controle de Threads (`-t`).
- [[gobuster-enumeracao-virtual-hosts-vhost-append-domain-filtros]] — Veja também: Gobuster Modo **`vhost`**: Descoberta de *Virtual Hosts* Internos em Reverse Proxies, **`--append-domain`** e Diferenciação de Respostas.

## Fontes
- [Gobuster Official GitHub — Modes (dir, vhost, dns, fuzz, s3, gcs, tftp) & CLI Reference](https://raw.githubusercontent.com/OJ/gobuster/master/README.md) — documentação oficial do Gobuster cobrindo todos os sete subcomandos, filtros de tamanho/status, mTLS, patterns e concorrência em Go; consultado em 2026-10-03.
- [Gobuster Official Wiki — Advanced Usage & Examples](https://github.com/OJ/gobuster/wiki) — wiki oficial do projeto Gobuster com exemplos práticos por subcomando; consultado em 2026-10-03.
- [Go Package Documentation — github.com/OJ/gobuster/v3](https://pkg.go.dev/github.com/OJ/gobuster/v3) — referência técnica dos pacotes internos do Gobuster v3 em Go; consultado em 2026-10-03.
