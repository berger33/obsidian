---
id: software.seguranca.tranche04.000357
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/httpx/main/README.md", "https://docs.projectdiscovery.io/opensource/httpx/overview", "https://github.com/projectdiscovery/retryablehttp-go/blob/main/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# ProjectDiscovery `httpx`: Extratores Regex (`-er`, `-ep`), Body Preview (`-bp`) e Cadeia de Redirecionamento (`-fr` / `- follow-redirects`)

## Em uma frase
O `httpx` permite extrair dados específicos de cabeçalhos e corpos HTTP durante a sondagem usando expressões regulares customizadas (`-er` / `-extract-regex`) ou presets integrados (`-ep` / `-extract-preset`), além de capturar *previews* do corpo (`-bp`) e a cadeia completa de redirecionamentos (`-location`, `-fr`, `-maxr`).

## Por que importa
Viabiliza identificar chaves de API vazadas em páginas públicas, versões de frameworks em comentários HTML, endereços de e-mail corporativos ou destinos finais de redirecionamentos SSO (`Location`) em uma única passada.

## Como funciona
A flag `-ep url,ipv4,mail` aciona padrões pré-compilados para extrair URLs, IPs e e-mails do corpo da resposta, enquanto `-er "AIza[0-9A-Za-z-_]{35}"` extrai padrões customizados e os grava no campo `.extracts` do JSONL. Quando `-fr` (`-follow-redirects`) ou `-fhr` (`-follow-host-redirects`, que restringe redirecionamentos ao mesmo host) está ativo, `-chain` registra cada salto intermediário.

## Exemplo
```bash
# Seguir redirecionamentos no mesmo host (-fhr) e extrair versões ou chaves via regex customizada
httpx -l live-hosts.txt \
  -fhr -maxr 5 -chain \
  -bp -er "v[0-9]+\.[0-9]+\.[0-9]+-rc[0-9]+" \
  -json -o redirects-and-extracts.jsonl
```

## Limites e trade-offs
Usar `-fr` (seguir redirecionamentos para qualquer domínio) em vez de `-fhr` (seguir apenas no mesmo host) pode fazer o `httpx` seguir redirecionamentos 302 para provedores de login de terceiros (Okta, Microsoft Login, Google) e classificar erroneamente a tecnologia do alvo como sendo a do IdP.

## Como verificar
Compare a saída de `-fr` vs `-fhr` em um endpoint protegido por SSO e confirme que `-fhr` preserva o escopo no domínio original.

## Conexões
- [[httpxpd-matchers-filters-status-length-string-regex-cdn-time]] — Veja também: ProjectDiscovery `httpx`: Filtragem Avançada com Matchers (`-mc`, `-ms`, `-mr`, `-mfc`) e Filters (`-fc`, `-fs`, `-fr`, `-fcdn`).
- [[httpxpd-otimizacao-rate-limit-threads-retries-timeout-waf-bypass]] — Veja também: ProjectDiscovery `httpx`: Controle de Concorrência (`-t`, `-rl`, `-rlm`), Retries, Timeout e Resiliência a WAF.
- [[httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit]] — Referência cruzada direta com httpxpd-arquitetura-probing-http-retryablehttp-multipurpose-toolkit.
- [[katana-extracao-campos-field-extraction-custom-regex-jsonl]] — Referência cruzada direta com katana-extracao-campos-field-extraction-custom-regex-jsonl.

## Fontes
- [ProjectDiscovery httpx GitHub — README.md (Multi-Purpose HTTP Toolkit, Supported Probes, Headless Screenshots, Matchers, Filters & Extractors)](https://raw.githubusercontent.com/projectdiscovery/httpx/main/README.md) — README oficial do projectdiscovery/httpx documentando a tabela de probes padrão e opcionais, flags de matchers/filters e captura headless; consultado em 2026-10-03.
- [ProjectDiscovery Official Documentation — httpx Overview (Architecture, Smart HTTPS-to-HTTP Fallback, WAF Retries & Pipeline Usage)](https://docs.projectdiscovery.io/opensource/httpx/overview) — Documentação oficial do httpx explicando o papel da ferramenta na transição entre descoberta de ativos e enriquecimento tecnológico; consultado em 2026-10-03.
- [ProjectDiscovery retryablehttp-go GitHub — README.md](https://github.com/projectdiscovery/retryablehttp-go/blob/main/README.md) — Biblioteca HTTP resiliente subjacente ao ProjectDiscovery httpx; consultado em 2026-10-03.
