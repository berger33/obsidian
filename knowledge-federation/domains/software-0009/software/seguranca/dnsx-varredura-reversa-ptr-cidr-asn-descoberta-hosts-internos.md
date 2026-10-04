---
id: software.seguranca.tranche09.000824
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/dnsx/main/README.md", "https://raw.githubusercontent.com/projectdiscovery/dnsx/main/go.mod", "https://docs.projectdiscovery.io/tools/dnsx/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `dnsx` **`-ptr` (`-resp-only`)**: Varredura de **DNS Reverso (`PTR` / `in-addr.arpa`)** a partir de Blocos CIDR e Números de **ASN (`AS...`)**

## Em uma frase
Quando você recebe um bloco de endereços IP (ex.: `192.0.2.0/24` na borda externa ou `10.20.0.0/16` em um pentest interno) ou um número de Sistema Autônomo (`AS1449`), a forma mais rápida e silenciosa de descobrir quais servidores existem naquela rede e quais são os seus nomes internos é consultar os registros de **DNS Reverso (`PTR`)**!

## Por que importa
Como o `dnsx` integra a biblioteca `projectdiscovery/mapcidr` e `asnmap`, você pode enviar um bloco CIDR ou um ASN diretamente via `echo "10.20.0.0/16" | dnsx -ptr -resp-only`!

## Como funciona
O `dnsx` expande automaticamente o bloco CIDR para todos os endereços IP individuais, formata as consultas reversas `.in-addr.arpa` / `.ip6.arpa` e retorna em segundos todos os hostnames configurados nos registros `PTR` daquela faixa!

## Exemplo
```bash
# Realizar varredura de DNS Reverso (PTR) sobre um bloco CIDR inteiro extraindo os hostnames descobertos
echo "10.20.0.0/16" | dnsx -silent -ptr -resp \
  -r 10.20.0.10 \
  -rl 500 \
  -o /cases/easm/internal_ptr_names.txt
```

## Limites e trade-offs
Em pentests internos corporativos (Active Directory / DNS Interno), apontar `-r <IP_DO_DNS_INTERNO>` e rodar `echo "10.0.0.0/8" | dnsx -ptr -resp` revela os nomes de servidores de banco de dados, controladores de domínio, cofres de backup e equipamentos de rede sem enviar um único pacote para os servidores finais (apenas consultando o servidor DNS!).

## Como verificar
Use `-resp-only` (`-ro`) se quiser extrair apenas os FQDNs retornados pelo `PTR` para canalizá-los diretamente para o `naabu` ou `httpx`.

## Conexões
- [[dnsx-forca-bruta-subdominios-wordlists-placeholders-fuzz]] — Veja também: `dnsx`: Força Bruta de Subdomínios (`-d` + `-w`) e **Substituição por Marcador `FUZZ`** em Qualquer Posição do Nome DNS.
- [[dnsx-auditoria-cname-subdomain-takeover-rcode-servfail-refused]] — Veja também: `dnsx`: Caça a **Subdomain Takeover (`dangling CNAME`)** e Filtragem por Código de Resposta DNS (**`-rcode noerror,nxdomain,servfail,refused`**).
- [[dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros]] — Referência cruzada direta com dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros.
- [[amass-descoberta-intel-asn-cidr-reverse-whois-organizacoes]] — Referência cruzada direta com amass-descoberta-intel-asn-cidr-reverse-whois-organizacoes.
- [[naabu-descoberta-hosts-ativos-host-discovery-sn-wn-icmp-arp-tcp]] — Referência cruzada direta com naabu-descoberta-hosts-ativos-host-discovery-sn-wn-icmp-arp-tcp.

## Fontes
- [ProjectDiscovery dnsx Official GitHub — Fast and Multi-Purpose DNS Toolkit](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/README.md) — repositório oficial do ProjectDiscovery dnsx cobrindo resolução em massa, filtragem de wildcard, força bruta, PTR reverso e rcodes; consultado em 2026-10-03.
- [ProjectDiscovery dnsx Official Documentation — CLI Flags & Pipeline Examples](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/go.mod) — documentação oficial do dnsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/dnsx](https://docs.projectdiscovery.io/tools/dnsx/overview) — referência técnica da biblioteca Go do ProjectDiscovery dnsx; consultado em 2026-10-03.
