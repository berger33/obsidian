---
id: software.seguranca.tranche08.000754
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

# Gobuster Modo **`dns`**: Enumeração Ativa de Subdomínios DNS (`--domain`), Resolvers Customizados (`--resolver`), Exibição de IPs/CNAMEs (`-i`, `-c`) e Wildcards

## Em uma frase
O modo **`gobuster dns`** realiza resolução ativa de nomes DNS (`A`/`AAAA`/`CNAME`) combinando uma wordlist de prefixos com o domínio alvo especificado por **`--domain`** (ou **`-d`** nas versões anteriores / `--do`).

## Por que importa
Por padrão, o `gobuster dns` imprime apenas os nomes de subdomínio encontrados; porém, passar as flags **`--show-ips` (`-i`)** e **`--show-cname` (`-c`)** enriquece imediatamente a saída com todos os endereços IPv4/IPv6 resolvidos e com o destino de registros **`CNAME`** — permitindo identificar em segundos candidatos a **Subdomain Takeover** (ex.: um `CNAME` apontando para um recurso `*.azurewebsites.net`, `*.s3.amazonaws.com` ou `*.github.io` desprovisionado)!

## Como funciona
Quando o domínio alvo possui um registro **DNS Wildcard (`*.exemplo.com.br -> 203.0.113.50`)**, o Gobuster detecta que um subdomínio UUID aleatório resolve para `203.0.113.50` e interrompe por segurança, a menos que `--wildcard` seja informado.

## Exemplo
```bash
# Enumerar subdominios via DNS exibindo tanto os enderecos IP (-i) quanto os registros CNAME (-c) usando resolver especifico
gobuster dns --domain exemplo.com.br \
  -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt \
  --resolver 1.1.1.1:53 \
  --show-ips --show-cname \
  -t 30 --timeout 3s -o /cases/pentest/gobuster_dns.txt
```

## Limites e trade-offs
Ao realizar enumeração ativa de subdomínios corporativos Internos (Split-Horizon DNS durante um pentest interno), aponte **`--resolver`** para o IP do controlador de domínio / servidor DNS interno da empresa (`10.x.x.x:53`), e **nunca** para resolvedores públicos (`8.8.8.8`), que não conhecem zonas privadas `.corp` / `.internal`.

## Como verificar
Verifique os registros `CNAME` reportados por `--show-cname` com `dig CNAME <subdominio>` para checar se o destino retorna `NXDOMAIN`.

## Conexões
- [[gobuster-enumeracao-virtual-hosts-vhost-append-domain-filtros]] — Veja também: Gobuster Modo **`vhost`**: Descoberta de *Virtual Hosts* Internos em Reverse Proxies, **`--append-domain`** e Diferenciação de Respostas.
- [[gobuster-enumeracao-cloud-buckets-s3-aws-gcs-google-cloud-storage]] — Veja também: Gobuster Modos **`s3`** e **`gcs`**: Descoberta de Buckets de Armazenamento em Nuvem (**AWS S3** e **Google Cloud Storage**) e Listagem de Objetos.
- [[gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz]] — Referência cruzada direta com gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz.

## Fontes
- [Gobuster Official GitHub — Modes (dir, vhost, dns, fuzz, s3, gcs, tftp) & CLI Reference](https://raw.githubusercontent.com/OJ/gobuster/master/README.md) — documentação oficial do Gobuster cobrindo todos os sete subcomandos, filtros de tamanho/status, mTLS, patterns e concorrência em Go; consultado em 2026-10-03.
- [Gobuster Official Wiki — Advanced Usage & Examples](https://github.com/OJ/gobuster/wiki) — wiki oficial do projeto Gobuster com exemplos práticos por subcomando; consultado em 2026-10-03.
- [Go Package Documentation — github.com/OJ/gobuster/v3](https://pkg.go.dev/github.com/OJ/gobuster/v3) — referência técnica dos pacotes internos do Gobuster v3 em Go; consultado em 2026-10-03.
