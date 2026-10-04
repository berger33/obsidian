---
id: software.seguranca.tranche17.001640
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://docs.sigstore.dev/cosign/overview/", "https://docs.sigstore.dev/cosign/verifying/verify/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Sigstore Cosign: Política de confiança no deploy

## Em uma frase
**Sigstore Cosign — Política de confiança no deploy:** A implantação precisa definir quais identidades, emissores e claims são aceitos para cada repositório e ambiente.

## Por que importa
O recorte de **política de confiança no deploy** ajuda a vincular origem, identidade do assinante e digest de um artefato antes de consumi-lo. A equipe registra risco, evidência e responsável.

## Como funciona
Para **política de confiança no deploy**, calcula ou usa o digest do artefato, cria assinatura ou atestação e permite verificar identidade, emissor e claims antes da implantação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Aplique verificação em um cluster de staging antes do prod e rejeite uma imagem sem signer permitido. Teste em staging autorizado.

## Limites e trade-offs
Uma verificação executada apenas no build pode ser contornada por outro caminho de publicação. Exceções exigem responsável e prazo.

## Como verificar
Demonstre que o admission path bloqueia artefato inválido, inclusive quando alguém tenta usar tag alternativa. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[opa-modelagem-da-decisao-em-rego]] — Complementa o tópico com open policy agent (opa): modelagem da decisão em rego.

## Fontes
- [Sigstore Cosign — Overview](https://docs.sigstore.dev/cosign/overview/) — visão oficial de assinatura, verificação e atestação com Cosign; consultado em 2026-10-04.
- [Sigstore Cosign — Verifying Signatures](https://docs.sigstore.dev/cosign/verifying/verify/) — referência oficial sobre verificação de assinatura e identidade OIDC; consultado em 2026-10-04.
