---
id: software.seguranca.tranche09.000830
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

# `dnsx` **`-srv`**: Enumeração de Registros **`SRV` (RFC 2782)** para Descoberta de Controladores **Active Directory (`_ldap._tcp`, `_kerberos._tcp`)**, SIP e XMPP

## Em uma frase
Em redes corporativas internas (Active Directory) e também em domínios externos que utilizam serviços federados (Microsoft 365, Telefonia SIP/VoIP, XMPP, Matrix, Minecraft, Consul/etcd), o protocolo DNS utiliza registros **`SRV` (`_servico._protocolo.dominio`, RFC 2782)** para anunciar exatamente em qual hostname e **porta TCP/UDP** cada serviço está rodando!

## Por que importa
Usando **`dnsx -srv -resp`**, um analista em um pentest interno descobre em 1 segundo todos os **Domain Controllers, servidores Kerberos (KDC) e Global Catalogs** da floresta Active Directory consultando `_ldap._tcp.dc._msdcs.<dominio_ad>`, `_kerberos._tcp.<dominio_ad>`, `_kpasswd._tcp.<dominio_ad>` e `_gc._tcp.<dominio_ad>`!

## Como funciona
Da mesma forma, na superfície externa, consultar `_sip._tls.<dominio>`, `_sipfederationtls._tcp.<dominio>` e `_autodiscover._tcp.<dominio>` revela servidores de comunicação unificada e Exchange híbridos expostos.

## Exemplo
```bash
# Descobrir todos os Domain Controllers e KDCs de um dominio Active Directory via registros SRV no dnsx
cat << 'EOF' | sed 's/DOMINIO/internal.corp/g' | dnsx -srv -resp -r 10.10.10.2
_ldap._tcp.DOMINIO
_ldap._tcp.dc._msdcs.DOMINIO
_kerberos._tcp.DOMINIO
_gc._tcp.DOMINIO
_autodiscover._tcp.DOMINIO
EOF
```

## Limites e trade-offs
Por que consultar registros `SRV` com o `dnsx` no início de um pentest interno é tão eficaz? Porque é **100% passivo perante os servidores finais** (consulta apenas o DNS na porta 53) e entrega imediatamente a lista exata de IPs/FQDNs dos Domain Controllers para alimentar o **BloodHound CE** ou **NetExec**!

## Como verificar
Verifique na resposta do `-srv -resp` a prioridade, o peso, a porta e o FQDN alvo retornados em cada registro `SRV`.

## Conexões
- [[dnsx-templates-saida-customizados-ot-json-omit-raw-stream]] — Veja também: `dnsx`: Formatação Avançada com **Output Templates (`-ot '{{host}} {{a}}'`)**, JSONL Enxuto (`-json -omit-raw`) e Modo **`-stream`**.
- [[dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros]] — Referência cruzada direta com dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros.

## Fontes
- [ProjectDiscovery dnsx Official GitHub — Fast and Multi-Purpose DNS Toolkit](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/README.md) — repositório oficial do ProjectDiscovery dnsx cobrindo resolução em massa, filtragem de wildcard, força bruta, PTR reverso e rcodes; consultado em 2026-10-03.
- [ProjectDiscovery dnsx Official Documentation — CLI Flags & Pipeline Examples](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/go.mod) — documentação oficial do dnsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/dnsx](https://docs.projectdiscovery.io/tools/dnsx/overview) — referência técnica da biblioteca Go do ProjectDiscovery dnsx; consultado em 2026-10-03.
