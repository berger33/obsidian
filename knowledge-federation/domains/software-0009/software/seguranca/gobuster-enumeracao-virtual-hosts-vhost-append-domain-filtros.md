---
id: software.seguranca.tranche08.000753
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

# Gobuster Modo **`vhost`**: Descoberta de *Virtual Hosts* Internos em Reverse Proxies, **`--append-domain`** e Diferenciação de Respostas

## Em uma frase
Muitas organizações apontam dezenas de subdomínios internos (`admin.corp.local`, `staging-api.corp.local`, `grafana.corp.local`) para o mesmo endereço IP de um balanceador Nginx/Envoy/HAProxy ou Ingress Kubernetes, **mas não publicam esses nomes no DNS público**: nesses casos, a enumeração DNS tradicional (`gobuster dns` / `subfinder`) não encontra nada!

## Por que importa
O modo **`gobuster vhost`** envia requisições HTTP/HTTPS diretamente para o endereço IP ou URL base do servidor alterando o cabeçalho HTTP **`Host: <palavra>.<dominio>`** a cada tentativa: quando o Nginx/Ingress reconhece um `server_name` configurado internamente, ele devolve uma resposta com status ou tamanho (`Size`) diferente do Virtual Host padrão (*default_server*).

## Como funciona
Atenção a uma mudança importante do Gobuster v3.2+: por padrão, o modo `vhost` usa a palavra da wordlist **literalmente** como cabeçalho `Host: <palavra>`, a menos que você passe a flag obrigatória **`--append-domain`** (ou que sua wordlist já contenha o domínio completo)!

## Exemplo
```bash
# Descobrir Virtual Hosts ocultos (nao publicados no DNS publico) em um Ingress/Reverse Proxy usando --append-domain
gobuster vhost -u https://10.20.30.40 \
  --domain internal.corp \
  --append-domain \
  -w /usr/share/seclists/Discovery/DNS/namelist.txt \
  --exclude-length 312 \
  -k -t 25 -o /cases/pentest/gobuster_vhosts.txt
```

## Limites e trade-offs
Observe o uso combinado de `-u https://10.20.30.40`, `--domain internal.corp` e `--append-domain`: isso garante que a conexão TCP/TLS vá para o IP `10.20.30.40` enquanto o cabeçalho HTTP envia `Host: <subdominio>.internal.corp`!

## Como verificar
Use `curl -ks -H "Host: dev-admin.internal.corp" https://10.20.30.40 -I` para confirmar manualmente cada Virtual Host descoberto pelo Gobuster.

## Conexões
- [[gobuster-enumeracao-diretorios-arquivos-dir-extensoes-status-exclude-length]] — Veja também: Gobuster Modo **`dir`**: Descoberta de Diretórios e Arquivos Ocultos, Extensões (`-x`), Filtros de Status (`-s` / `-b`) e **`--exclude-length`**.
- [[gobuster-enumeracao-subdominios-dns-resolvers-wildcard-cname-ip]] — Veja também: Gobuster Modo **`dns`**: Enumeração Ativa de Subdomínios DNS (`--domain`), Resolvers Customizados (`--resolver`), Exibição de IPs/CNAMEs (`-i`, `-c`) e Wildcards.
- [[gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz]] — Referência cruzada direta com gobuster-arquitetura-concorrencia-go-subcomandos-dir-dns-vhost-s3-gcs-fuzz.

## Fontes
- [Gobuster Official GitHub — Modes (dir, vhost, dns, fuzz, s3, gcs, tftp) & CLI Reference](https://raw.githubusercontent.com/OJ/gobuster/master/README.md) — documentação oficial do Gobuster cobrindo todos os sete subcomandos, filtros de tamanho/status, mTLS, patterns e concorrência em Go; consultado em 2026-10-03.
- [Gobuster Official Wiki — Advanced Usage & Examples](https://github.com/OJ/gobuster/wiki) — wiki oficial do projeto Gobuster com exemplos práticos por subcomando; consultado em 2026-10-03.
- [Go Package Documentation — github.com/OJ/gobuster/v3](https://pkg.go.dev/github.com/OJ/gobuster/v3) — referência técnica dos pacotes internos do Gobuster v3 em Go; consultado em 2026-10-03.
