---
id: software.seguranca.tranche08.000756
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

# Gobuster Modo **`fuzz`**: Fuzzing de Parâmetros Query/REST, Cabeçalhos HTTP e Corpo de Requisição com a Palavra-Chave **`FUZZ`**

## Em uma frase
Introduzido no Gobuster v3.1+, o modo **`gobuster fuzz`** estende a ferramenta muito além de simples diretórios: você pode posicionar o marcador literal **`FUZZ`** em **qualquer lugar da URL (`-u`)**, dentro de **qualquer cabeçalho HTTP (`-H "X-Custom: FUZZ"`)**, na **string de autenticação Basic Auth (`-U` / `-P`)** ou dentro do **corpo da requisição POST/PUT (`-B` / `--body`)**!

## Por que importa
Isso permite usar o mesmo binário do Gobuster para descobrir parâmetros GET/POST ocultos (`?FUZZ=1`), enumerar IDs de objetos ou endpoints de API REST (`/api/v1/users/FUZZ/profile`), testar cabeçalhos de bypass de proxy (`X-Forwarded-Host: FUZZ`) ou fazer fuzzing de valores em payloads JSON.

## Como funciona
Assim como no modo `dir`, o `gobuster fuzz` suporta `--exclude-length` e `-b` para descartar respostas idênticas ao comportamento padrão.

## Exemplo
```bash
# Executar fuzzing de nomes de parametros GET ocultos em um endpoint de API filtrando o tamanho da resposta padrao
gobuster fuzz -u "https://api.internal.corp/v1/debug?FUZZ=true" \
  -w /usr/share/seclists/Discovery/Web-Content/burp-parameter-names.txt \
  --exclude-length 48 \
  -b 404,400 \
  -t 20 -o /cases/pentest/gobuster_param_fuzz.txt
```

## Limites e trade-offs
Lembre-se de que no modo `gobuster fuzz`, a palavra **`FUZZ` (em letras maiúsculas)** é obrigatória em pelo menos um dos campos (`-u`, `-H`, `--body`, `-U`, `-P`); se você esquecer de incluir `FUZZ`, o Gobuster retornará um erro de validação antes de iniciar.

## Como verificar
Inspecione os tamanhos de resposta (`[Size: ...]`) diferentes do padrão para identificar quais parâmetros alteraram a lógica de execução do backend.

## Conexões
- [[gobuster-enumeracao-cloud-buckets-s3-aws-gcs-google-cloud-storage]] — Veja também: Gobuster Modos **`s3`** e **`gcs`**: Descoberta de Buckets de Armazenamento em Nuvem (**AWS S3** e **Google Cloud Storage**) e Listagem de Objetos.
- [[gobuster-enumeracao-tftp-equipamentos-rede-voip-firmwares-configs]] — Veja também: Gobuster Modo **`tftp`**: Auditoria de Servidores **TFTP (Porta 69/UDP)** em Redes Internas, Telefonia VoIP e Provisionamento PXE/Cisco.
- [[gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz]] — Referência cruzada direta com gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz.
- [[gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length]] — Referência cruzada direta com gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length.

## Fontes
- [Gobuster Official GitHub — Modes (dir, vhost, dns, fuzz, s3, gcs, tftp) & CLI Reference](https://raw.githubusercontent.com/OJ/gobuster/master/README.md) — documentação oficial do Gobuster cobrindo todos os sete subcomandos, filtros de tamanho/status, mTLS, patterns e concorrência em Go; consultado em 2026-10-03.
- [Gobuster Official Wiki — Advanced Usage & Examples](https://github.com/OJ/gobuster/wiki) — wiki oficial do projeto Gobuster com exemplos práticos por subcomando; consultado em 2026-10-03.
- [Go Package Documentation — github.com/OJ/gobuster/v3](https://pkg.go.dev/github.com/OJ/gobuster/v3) — referência técnica dos pacotes internos do Gobuster v3 em Go; consultado em 2026-10-03.
