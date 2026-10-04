---
id: software.seguranca.tranche09.000827
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

# `dnsx`: Teste em Massa de **Transferência de Zona DNS (`-axfr`)** e Rastreamento da Cadeia de Delegação Autoritativa (**`-trace`**)

## Em uma frase
A **Transferência de Zona DNS (`AXFR`, RFC 5936 sobre porta 53/TCP)** é o mecanismo usado por servidores DNS secundários (slaves) para copiar o arquivo completo da zona a partir do servidor primário (master); porém, se um servidor autoritativo estiver mal configurado permitindo `AXFR` para qualquer endereço IP (`allow-transfer { any; };`), qualquer atacante na internet consegue baixar **100% dos registros DNS da empresa em uma única requisição TCP**!

## Por que importa
Passar a flag **`-axfr`** ao `dnsx` consulta automaticamente os servidores autoritativos (`NS`) de cada domínio da lista e testa se algum deles aceita uma requisição `AXFR`, despejando os registros retornados no JSON!

## Como funciona
E quando você precisa diagnosticar problemas de delegação DNS (como **Lame Delegation**, onde um dos servidores `NS` listados no registro pai não responde ou não se reconhece como autoritativo para a zona), a flag **`-trace`** (com `-trace-max-recursion`) percorre a árvore desde os Root Servers (`.`) até os autoritativos finais!

## Exemplo
```bash
# Testar transferencia de zona DNS (AXFR) e rastrear a cadeia de delegacao (-trace) nos dominios da organizacao
dnsx -l /cases/easm/company_root_domains.txt \
  -axfr -resp \
  -json -o /cases/easm/axfr_audit.jsonl

echo "app.exemplo.com.br" | dnsx -a -trace
```

## Limites e trade-offs
Se o `dnsx -axfr` tiver sucesso em qualquer servidor `NS` público, trate o achado como uma falha de exposição de infraestrutura e restrinja imediatamente o `allow-transfer` no BIND/PowerDNS/Windows DNS apenas aos IPs dos servidores secundários autenticados por chave criptográfica **TSIG (RFC 8945)**.

## Como verificar
Verifique no arquivo `axfr_audit.jsonl` se o objeto `"axfr"` retornou registros de zona.

## Conexões
- [[dnsx-auditoria-seguranca-email-spf-dmarc-dkim-caa-txt-mx]] — Veja também: `dnsx`: Auditoria em Lote de Segurança de E-mail (**SPF / DMARC em `-txt`**, **`-mx`**) e Governança de Certificados (**`-caa`**, **`-soa`**).
- [[dnsx-resolvedores-customizados-doh-dot-rate-limit-retry-timeout]] — Veja também: `dnsx`: Configuração de **Resolvedores DNS-over-HTTPS (`DoH`) e DNS-over-TLS (`DoT`)**, Controle de Taxa (`-rl`), `-retry` e `-timeout`.
- [[dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros]] — Referência cruzada direta com dnsx-arquitetura-toolkit-dns-retryabledns-doh-dot-multi-registros.
- [[dnsx-auditoria-cname-subdomain-takeover-rcode-servfail-refused]] — Referência cruzada direta com dnsx-auditoria-cname-subdomain-takeover-rcode-servfail-refused.
- [[amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados]] — Referência cruzada direta com amass-enumeracao-passiva-ativa-normal-ciclo-dns-certificados.

## Fontes
- [ProjectDiscovery dnsx Official GitHub — Fast and Multi-Purpose DNS Toolkit](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/README.md) — repositório oficial do ProjectDiscovery dnsx cobrindo resolução em massa, filtragem de wildcard, força bruta, PTR reverso e rcodes; consultado em 2026-10-03.
- [ProjectDiscovery dnsx Official Documentation — CLI Flags & Pipeline Examples](https://raw.githubusercontent.com/projectdiscovery/dnsx/main/go.mod) — documentação oficial do dnsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/dnsx](https://docs.projectdiscovery.io/tools/dnsx/overview) — referência técnica da biblioteca Go do ProjectDiscovery dnsx; consultado em 2026-10-03.
