---
id: software.seguranca.tranche08.000755
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

# Gobuster Modos **`s3`** e **`gcs`**: Descoberta de Buckets de Armazenamento em Nuvem (**AWS S3** e **Google Cloud Storage**) e Listagem de Objetos

## Em uma frase
Vazamentos de dados em nuvem frequentemente decorrem de buckets **Amazon S3** ou **Google Cloud Storage (GCS)** criados com nomes previsíveis (`empresa-backups`, `empresa-prod-assets`, `empresa-faturas`, `empresa-terraform-state`) e permissões de leitura/listagem públicas (`AllUsers` / `AuthenticatedUsers`).

## Por que importa
O Gobuster inclui dois modos dedicados para auditoria de superfície de armazenamento em nuvem: **`gobuster s3 -w <wordlist>`** (que consulta os endpoints XML da AWS S3 e interpreta automaticamente as respostas `NoSuchBucket`, `AccessDenied` e `ListBucketResult`) e **`gobuster gcs -w <wordlist>`** (que consulta a API JSON do Google Cloud Storage).

## Como funciona
Com a flag **`-m` (`--max-files-to-list`)**, quando o Gobuster encontra um bucket S3 ou GCS com listagem pública habilitada, ele já exibe os primeiros $N$ nomes de arquivos contidos no bucket para comprovar a criticidade do achado sem precisar baixar terabytes de dados!

## Exemplo
```bash
# Auditar a existencia e permissoes de buckets AWS S3 e Google Cloud Storage (GCS) a partir de uma wordlist de prefixos da empresa
gobuster s3 -w /cases/pentest/corp_bucket_permutations.txt \
  --max-files-to-list 5 \
  -t 15 -o /cases/pentest/discovered_s3_buckets.txt

gobuster gcs -w /cases/pentest/corp_bucket_permutations.txt \
  --max-files-to-list 5 \
  -t 15 -o /cases/pentest/discovered_gcs_buckets.txt
```

## Limites e trade-offs
Ao gerar a wordlist para `gobuster s3` e `gobuster gcs`, combine a marca/sigla da organização com sufixos padrão de ambientes (`-dev`, `-staging`, `-prod`, `-backup`, `-logs`, `-public`, `-static`, `-tfstate`, `-data`) respeitando as regras de nomenclatura de buckets (apenas letras minúsculas, números e hífens).

## Como verificar
Para cada bucket retornado com status público, notifique imediatamente a equipe de Cloud Security para aplicar **S3 Block Public Access** / **GCS Public Access Prevention**.

## Conexões
- [[gobuster-enumeracao-subdominios-dns-resolvers-wildcard-cname-ip]] — Veja também: Gobuster Modo **`dns`**: Enumeração Ativa de Subdomínios DNS (`--domain`), Resolvers Customizados (`--resolver`), Exibição de IPs/CNAMEs (`-i`, `-c`) e Wildcards.
- [[gobuster-modo-fuzz-marcador-customizado-url-headers-body-parametros]] — Veja também: Gobuster Modo **`fuzz`**: Fuzzing de Parâmetros Query/REST, Cabeçalhos HTTP e Corpo de Requisição com a Palavra-Chave **`FUZZ`**.
- [[gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz]] — Referência cruzada direta com gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz.
- [[amass-descoberta-intel-asn-cidr-reverse-whois-organizacoes]] — Referência cruzada direta com amass-descoberta-intel-asn-cidr-reverse-whois-organizacoes.

## Fontes
- [Gobuster Official GitHub — Modes (dir, vhost, dns, fuzz, s3, gcs, tftp) & CLI Reference](https://raw.githubusercontent.com/OJ/gobuster/master/README.md) — documentação oficial do Gobuster cobrindo todos os sete subcomandos, filtros de tamanho/status, mTLS, patterns e concorrência em Go; consultado em 2026-10-03.
- [Gobuster Official Wiki — Advanced Usage & Examples](https://github.com/OJ/gobuster/wiki) — wiki oficial do projeto Gobuster com exemplos práticos por subcomando; consultado em 2026-10-03.
- [Go Package Documentation — github.com/OJ/gobuster/v3](https://pkg.go.dev/github.com/OJ/gobuster/v3) — referência técnica dos pacotes internos do Gobuster v3 em Go; consultado em 2026-10-03.
